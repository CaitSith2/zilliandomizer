from typing import Dict, Iterable, List, Tuple

from zilliandomizer.map_gen.base_maker import BaseMaker, Node
from zilliandomizer.map_gen.door_decider import DE, Desc, make_edge_descriptions
from zilliandomizer.room_gen.common import Coord, EdgeDoors, RoomData, TOP_LEFT, TOP_RIGHT
from zilliandomizer.room_gen.data import GEN_ROOMS

_red_right_generate = {
    0x2b, 0x2c, 0x2d,       0x2f,
    0x33, 0x34,       0x36, 0x37,
    0x3b, 0x3c, 0x3d, 0x3e, 0x3f,
    0x43, 0x44, 0x45, 0x46, 0x47,
    0x4b, 0x4c, 0x4d,       0x4f,
}


def room_data_exits_from_descs(descs: Iterable[Desc]) -> Tuple[List[Coord], EdgeDoors]:
    """
    `(exits, edge_doors)` (parameters to `RoomData`)

    first value in `descs` should be the entrance
    """
    out: List[Coord] = []
    edge_doors: EdgeDoors = ([], [])
    for desc in descs:
        if desc.de is DE.door:
            if desc.x == 0x00:
                x = 0
            else:
                assert desc.x == 0xf0, f"{desc.x=}"
                x = 12
            y = desc.y + 1
            edge_doors[x // 12].append(y)
        else:
            assert desc.de is DE.elevator  # TODO: assert_type()
            x = (desc.x >> 4) - 1
            if desc.y == 0:
                y = 1
            else:
                assert desc.y == 5, f"{desc=}"
                y = 5
        assert y >= 0 and x >= 0, f"{descs=}"
        out.append((y, x))
    return out, edge_doors


def make_room_gen_data(bm: BaseMaker) -> Dict[int, RoomData]:
    out = GEN_ROOMS.copy()
    edge_descriptions = make_edge_descriptions(bm)

    for row in range(5, 5 + bm.height):
        for col in range(3, 3 + bm.width):
            map_index = row * 8 + col
            if map_index in out:
                # delete vanilla
                del out[map_index]
            if map_index not in _red_right_generate:
                continue
            node = Node(row - 5, col - 3)  # TODO: get these 5, 3 magic numbers from BaseMaker
            outs = edge_descriptions[node]
            exits, edge_doors = room_data_exits_from_descs(outs.values())

            if map_index in GEN_ROOMS:
                computer = GEN_ROOMS[map_index].computer
            else:
                assert map_index in {44, 68}, f"{map_index=}"
                computer = True

            computer_opens_door = computer and map_index != 79  # bottom right red room  # TODO: logic for whole base

            if len(exits) == 1:
                # dead end
                if computer_opens_door:
                    y, x = exits[0]
                    if y > 3:
                        # entrance at bottom of room
                        exits.append(bm.random.choice((TOP_RIGHT, TOP_LEFT)))
                    else:
                        # entrance at top of room
                        if x < 7:
                            exits.append(TOP_RIGHT)
                        else:
                            exits.append(TOP_LEFT)
                    # TODO: make sure canister is placed in this corner

            # exits to red elevator, all need space before door to prevent softlock in escape
            no_space: List[Coord]
            if map_index in {0x33, 0x43, 0x4b}:
                no_space = [(3, 0)]
            else:
                no_space = []

            out[map_index] = RoomData(exits, computer, no_space, edge_doors)

    return out
