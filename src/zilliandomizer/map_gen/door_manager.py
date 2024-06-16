from collections import defaultdict
from enum import IntEnum
from typing import Dict, List, Literal, Tuple

from zilliandomizer.low_resources import rom_info
from zilliandomizer.utils.deterministic_set import DetSet

BANK_4_OFFSET = 0x8000

DoorStatusIndex = Tuple[int, int]
""" low byte of address and bit mask for whether a door is opened """


class DoorSprite(IntEnum):
    """
    - B blue
    - R red
    - P paperclip
    ---
    - L door in left half of large tile (usually leading to the right)
    - R door in right half of large tile (usually leading to the left)
    - D elevator at bottom to go down
    - U elevator at top to go up
    """
    BL = 0
    BR = 5
    BD = 30
    BU = 31
    RL = 10
    RR = 15
    RD = 32
    RU = 33
    PL = 20
    PR = 25
    PD = 34
    PU = 35

    @staticmethod
    def get_door(map_index: int, x: int) -> "DoorSprite":
        """ `x` in door data structure units (4 pixels) """
        assert (x & 1) == 0, f"{x=}"
        if map_index < 40:
            if x & 2:
                return DoorSprite.BR
            else:
                return DoorSprite.BL
        if map_index < 80:
            if x & 2:
                return DoorSprite.RR
            else:
                return DoorSprite.RL
        if x & 2:
            return DoorSprite.PR
        else:
            return DoorSprite.PL

    @staticmethod
    def get_elevator(map_index: int, y: Literal[0, 5]) -> "DoorSprite":
        """ `y` in door data structure units (0 top, 5 bottom) """
        if map_index < 40:
            if y == 0:
                return DoorSprite.BU
            else:
                return DoorSprite.BD
        if map_index < 80:
            if y == 0:
                return DoorSprite.RU
            else:
                return DoorSprite.RD
        if y == 0:
            return DoorSprite.PU
        else:
            return DoorSprite.PD


class DoorManager:
    original_statuses: Dict[int, DoorStatusIndex]
    """
    This room is the first time these statuses are opened.

    (only newly created doors)
    """
    freed_statuses: DetSet[DoorStatusIndex]
    """ this `DoorStatusIndex` existed in vanilla, but all its doors have been deleted """
    status_reference_counts: Dict[DoorStatusIndex, List[int]]
    """
    which room has a door data structure that
    shares the same share the same info on whether the door is open or not

    the index is `(a, b)` - the first 2 bytes of the door data structure
    """
    doors: Dict[int, List[bytes]]
    """
    map_index: [[a, b, x, y, t], ...]
        - a - byte index pointing to data of whether the door is open
        - b - bit mask ^
        - x - `<< 2` for (left) x pixel of door (or elevator)
        - y - 0 top row (both door and elevator), 4 door on bottom, 5 elevator on bottom
        - t - `DoorSprite`
    """

    def __init__(self) -> None:
        self.original_statuses = {}
        self.freed_statuses = DetSet()
        self.status_reference_counts = defaultdict(list)
        from copy import deepcopy
        from .door_data import doors
        self.doors = defaultdict(list, deepcopy(doors))

        self._fill()

    def _fill(self) -> None:
        for map_index, door_list in self.doors.items():
            for door_data in door_list:
                a, b, _, _, _ = door_data
                status: DoorStatusIndex = (a, b)
                self.status_reference_counts[status].append(map_index)
                # map_index 65 or 90 is the only place where more than 2 doors all share the same status bit
                # (because no computer to open them)
                assert (
                    len(self.status_reference_counts[status]) <= 2
                    or status == (19, 1)
                    or status == (37, 1)
                ), f"{map_index=} {status=}"

    def del_room(self, map_index: int) -> None:
        """ and matching status references in other rooms (elevator in destination room) """
        if map_index in self.doors:
            door_list = self.doors[map_index]
            while len(door_list):
                door = door_list.pop()
                a, b, _, _, _ = door
                status: DoorStatusIndex = (a, b)
                for each_map_index in self.status_reference_counts[status]:
                    self.doors[each_map_index] = [
                        each_door
                        for each_door in self.doors[each_map_index]
                        if not each_door.startswith(bytes(status))
                    ]
                self.status_reference_counts[status] = []
                assert status not in self.freed_statuses, f"{map_index=} {status=}"
                self.freed_statuses.add(status)

    def add_door(self, map_index: int, y_large: int, x_pixel: int, opened_by: int) -> None:
        status = self._get_available_status(opened_by)
        x_door = x_pixel >> 2
        sprite = DoorSprite.get_door(map_index, x_door)
        door_data = bytes((status[0], status[1], x_door, y_large, sprite))
        self.doors[map_index].append(door_data)
        self.status_reference_counts[status].append(map_index)

    def add_elevator(self, map_index: int, y_large: Literal[0, 5], x_pixel: int, opened_by: int) -> None:
        """ both in this room and destination room """
        status = self._get_available_status(opened_by)
        x_door = x_pixel >> 2
        sprite = DoorSprite.get_elevator(map_index, y_large)
        door_data = bytes((status[0], status[1], x_door, y_large, sprite))
        self.doors[map_index].append(door_data)
        self.status_reference_counts[status].append(map_index)

        dest_y: Literal[0, 5]
        if y_large == 0:
            # going up
            dest_map_index = map_index - 8
            dest_y = 5
        else:  # doing down
            assert y_large == 5, f"{y_large=}"  # TODO: assert_type
            dest_map_index = map_index + 8
            dest_y = 0
        dest_sprite = DoorSprite.get_elevator(dest_map_index, dest_y)
        dest_door_data = bytes((status[0], status[1], x_door, dest_y, dest_sprite))
        self.doors[dest_map_index].append(dest_door_data)
        self.status_reference_counts[status].append(dest_map_index)

    def _get_available_status(self, opening_map_index: int) -> DoorStatusIndex:
        """ and remove from freed """
        status = self.original_statuses.get(opening_map_index)
        if status:
            return status
        if len(self.freed_statuses):
            status = self.freed_statuses.pop()
            self.original_statuses[opening_map_index] = status
            return status
        index = 3
        while True:
            # In vanilla, none use more than 3 bits (1, 2, 4), so I don't know if it's safe to use more.
            for bit in (1, 2, 4):
                status = (index, bit)
                if len(self.status_reference_counts[status]) == 0:
                    self.original_statuses[opening_map_index] = status
                    return status
            index += 1

    def get_writes(self) -> Dict[int, int]:
        null_address = rom_info.door_data_begin_13ce8
        null_banked_lo = null_address & 0xff
        null_banked_hi = (null_address - BANK_4_OFFSET) // 256
        tr = {null_address: 0}
        address = null_address + 1

        for map_index in range(136):
            row = map_index // 8
            col = map_index % 8
            door_data_pointer_address = rom_info.terrain_index_13725 + 65 * row + 8 * col + 5
            doors = self.doors.get(map_index, [])
            if len(doors) == 0:
                # print(f"room {map_index} no doors")
                tr[door_data_pointer_address] = null_banked_lo
                tr[door_data_pointer_address + 1] = null_banked_hi
            else:
                # print(f"room {map_index} {len(doors)} doors")
                banked_data_address = address - BANK_4_OFFSET
                banked_data_lo = banked_data_address & 0xff
                banked_data_hi = banked_data_address // 256
                tr[door_data_pointer_address] = banked_data_lo
                tr[door_data_pointer_address + 1] = banked_data_hi

                tr[address] = len(doors)
                address += 1
                for door in doors:
                    for b in door:
                        tr[address] = b
                        address += 1

        return tr
