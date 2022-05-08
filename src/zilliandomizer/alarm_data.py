from dataclasses import dataclass
from random import randint
from typing import Dict, FrozenSet, List, Tuple, Generator

from zilliandomizer.terrain_tiles import Tile


ALARM_ROOMS: List[int] = [
    0x0b, 0x0f,
    0x17,
    0x1a, 0x1c,
    0x21, 0x22, 0x24,
    0x2c, 0x2d, 0x2f,  # TODO: fix enemy entrance of 0x2c (Apple's room)
    0x33,
    0x39, 0x3b, 0x3d, 0x3f,
    0x41, 0x43, 0x44, 0x45,  # TODO: decide whether to change enemy entrance of 0x44
    0x4b, 0x4d, 0x4f,
    0x51, 0x52, 0x54,
    0x59, 0x5a, 0x5b,
    0x64, 0x66,
    0x69, 0x6e,
    0x72, 0x75,
    # no alarm lines in bottom 2 rows
]

# TODO: list of alarm rooms ordered by compressed length variance from lowest to highest
# to adjust while looking at how many bytes are used

fs = frozenset


@dataclass
class Alarm:
    """ can look at vertical and the number of blocks to see how expensive it is """
    id: str
    """ referenced by `disables` and `lessens` """
    vertical: bool
    top_left: Tuple[int, int]
    """" (row, col) """
    length: int
    """ how many blocks is this alarm sensor in """
    vanilla: bool
    """ this alarm is present in vanilla """
    disables: FrozenSet[str]
    """
    ids of other alarms in the room
    that can't be present at the same time as this one
    """
    lessens: FrozenSet[str]
    """
    ids of other alarms in the room
    that are less likely to be present at the same time as this one
    """
    vary: int = 0
    """
    how many spaces this line
    can be moved (perpendicular to the line - right or down) and be equivalent to the same line
    """
    vanilla_vary: int = 0
    """ the varied position this alarm is present in vanilla, ignored if not vanilla """

    def block_iter(self) -> Generator[Tuple[int, bool], None, None]:
        """
        yield (block_index, erase)

        if erase, this is where a vanilla line goes and it needs to be erased
        if not erase, this is where vary chose to put the alarm line
        """
        row, col = self.top_left
        vary = randint(0, self.vary)
        if self.vanilla and vary != self.vanilla_vary:
            # need to erase vanilla
            vanilla_row = row
            vanilla_col = col
            if self.vertical:
                vanilla_col += self.vanilla_vary
            else:
                vanilla_row += self.vanilla_vary
            block_index = vanilla_row * 16 + vanilla_col
            for _ in range(self.length):
                assert block_index < 96, f"{self.id} {block_index}"
                yield block_index, True
                if self.vertical:
                    block_index += 16
                else:
                    block_index += 1
            # done erasing vanilla

        # now send the blocks that vary chose
        if self.vertical:
            col += vary
        else:
            row += vary
        block_index = row * 16 + col
        for _ in range(self.length):
            assert block_index < 96, f"{self.id} {block_index}"
            yield block_index, False
            if self.vertical:
                block_index += 16
            else:
                block_index += 1


to_vertical = {
    # ceiling
    Tile.b_ceiling: Tile.b_ceiling_v,
    Tile.b_ceiling_v: Tile.b_ceiling_v,

    Tile.r_light_ceiling: Tile.r_light_ceiling_v,
    Tile.r_light_ceiling_v: Tile.r_light_ceiling_v,

    Tile.p_ceiling: Tile.p_ceiling_v,
    Tile.p_ceiling_v: Tile.p_ceiling_v,

    # space
    Tile.b_space: Tile.b_space_v,
    Tile.b_space_v: Tile.b_space_v,
    Tile.b_space_h: Tile.b_space_v,

    Tile.r_dark_space: Tile.r_dark_space_v,
    Tile.r_dark_space_v: Tile.r_dark_space_v,
    Tile.r_dark_space_h: Tile.r_dark_space_v,

    Tile.p_space: Tile.p_space_v,
    Tile.p_space_v: Tile.p_space_v,
    Tile.p_space_h: Tile.p_space_v,

    # floor
    Tile.b_floor: Tile.b_floor_v,
    Tile.b_floor_v: Tile.b_floor_v,
    Tile.b_floor_h: Tile.b_floor_v,

    Tile.r_dark_floor: Tile.r_dark_floor_v,
    Tile.r_dark_floor_v: Tile.r_dark_floor_v,
    Tile.r_dark_floor_h: Tile.r_dark_floor_v,

    Tile.p_floor: Tile.p_floor_v,
    Tile.p_floor_v: Tile.p_floor_v,
    Tile.p_floor_h: Tile.p_floor_v,
}

to_horizontal = {
    # space
    Tile.b_space: Tile.b_space_h,
    Tile.b_space_v: Tile.b_space_h,
    Tile.b_space_h: Tile.b_space_h,

    Tile.r_light_space: Tile.r_light_space_h,
    Tile.r_light_space_h: Tile.r_light_space_h,

    Tile.r_dark_space: Tile.r_dark_space_h,
    Tile.r_dark_space_v: Tile.r_dark_space_h,
    Tile.r_dark_space_h: Tile.r_dark_space_h,

    Tile.p_space: Tile.p_space_h,
    Tile.p_space_v: Tile.p_space_h,
    Tile.p_space_h: Tile.p_space_h,

    # floor
    Tile.b_floor: Tile.b_floor_h,
    Tile.b_floor_v: Tile.b_floor_h,
    Tile.b_floor_h: Tile.b_floor_h,

    Tile.r_light_floor: Tile.r_light_floor_h,
    Tile.r_light_floor_h: Tile.r_light_floor_h,

    Tile.r_dark_floor: Tile.r_dark_floor_h,
    Tile.r_dark_floor_v: Tile.r_dark_floor_h,
    Tile.r_dark_floor_h: Tile.r_dark_floor_h,

    Tile.p_floor: Tile.p_floor_h,
    Tile.p_floor_v: Tile.p_floor_h,
    Tile.p_floor_h: Tile.p_floor_h,
}

to_none = {
    # ceiling
    Tile.b_ceiling: Tile.b_ceiling,
    Tile.b_ceiling_v: Tile.b_ceiling,

    Tile.r_light_ceiling: Tile.r_light_ceiling,
    Tile.r_light_ceiling_v: Tile.r_light_ceiling,

    Tile.p_ceiling: Tile.p_ceiling,
    Tile.p_ceiling_v: Tile.p_ceiling,

    # space
    Tile.b_space: Tile.b_space,
    Tile.b_space_v: Tile.b_space,
    Tile.b_space_h: Tile.b_space,

    Tile.r_light_space: Tile.r_light_space,
    Tile.r_light_space_h: Tile.r_light_space,

    Tile.r_dark_space: Tile.r_dark_space,
    Tile.r_dark_space_v: Tile.r_dark_space,
    Tile.r_dark_space_h: Tile.r_dark_space,

    Tile.p_space: Tile.p_space,
    Tile.p_space_v: Tile.p_space,
    Tile.p_space_h: Tile.p_space,

    # floor
    Tile.b_floor: Tile.b_floor,
    Tile.b_floor_v: Tile.b_floor,
    Tile.b_floor_h: Tile.b_floor,

    Tile.r_light_floor: Tile.r_light_floor,
    Tile.r_light_floor_h: Tile.r_light_floor,

    Tile.r_dark_floor: Tile.r_dark_floor,
    Tile.r_dark_floor_v: Tile.r_dark_floor,
    Tile.r_dark_floor_h: Tile.r_dark_floor,

    Tile.p_floor: Tile.p_floor,
    Tile.p_floor_v: Tile.p_floor,
    Tile.p_floor_h: Tile.p_floor,
}

alarm_data: Dict[int, List[Alarm]] = {
    0x0b: [
        Alarm("plat1top", True, (0, 5), 3,
              False, fs(), fs(["plat1bot", "hor-high", "hor-mid"]), 1),
        Alarm("plat1bot", True, (3, 4), 3,
              True, fs(["hor-mid"]), fs(["plat1top", "hor-high"]), 2, 1),
        Alarm("hor-mid", False, (4, 1), 7,
              False, fs(["plat1bot"]), fs(["plat1top", "plat2top", "plat2bot"])),
        Alarm("hor-high", False, (3, 1), 3, False, fs(), fs(["plat1top", "plat1bot"])),
        Alarm("plat2top", True, (0, 9), 4, False, fs(), fs(["hor-mid", "plat2bot"]), 1),
        Alarm("plat2bot", True, (4, 8), 2, False, fs(), fs(["hor-mid", "plat2top"]), 2),
        Alarm("plat3top", True, (0, 12), 5, False, fs(), fs(["plat3bot"]), 1),
        Alarm("plat3bot", True, (5, 13), 1, False, fs(), fs(["plat3top"]))
    ],
    0x0f: [
        Alarm("vTopLeft", True, (0, 2), 2, False, fs(), fs(), 1),
        # can't use vary on this because it changes disable
        Alarm("vMidLeftOri", True, (2, 2), 2, True, fs(), fs(["vMidLeft"])),
        Alarm("vMidLeft", True, (2, 3), 2, False, fs(["hTopLeft"]), fs(["vMidLeftOri"])),
        Alarm("vTopMid", True, (0, 10), 2, False, fs(), fs(["hTopLeft", "hMidRight"]), 1),
        Alarm("vBotMid", True, (4, 9), 2, False, fs(["hBotRight"]), fs()),
        Alarm("vMidRight", True, (3, 12), 2, False, fs(["hBotRight", "hMidRight"]), fs()),
        Alarm("vBotRight", True, (4, 14), 2, False, fs(), fs(["hBotRight"])),
        Alarm("hTopLeft", False, (2, 3), 7,
              False, fs(["vMidLeft"]), fs(["vMidLeftOri", "hBotLeft", "vTopMid"])),
        Alarm("hBotLeft", False, (4, 3), 3,
              False, fs(), fs(["hTopLeft", "vTopMid", "hMidRight", "hBotRight"])),
        Alarm("hMidRight", False, (3, 12), 3,
              False, fs(["vMidRight"]), fs(["hTopLeft", "vTopMid", "hBotLeft", "hBotRight"])),
        Alarm("hBotRight", False, (4, 9), 5,
              False, fs(["vBotMid", "vMidRight"]), fs(["hTopLeft", "vTopMid", "hBotLeft", "hMidRight"]))
    ],
    0x17: [
        Alarm("v-top-left", True, (0, 4), 2, False, fs(), fs(["h-mid", "h-bot"]), 2),
        Alarm("v-top-right", True, (0, 9), 2, True, fs(), fs(["h-mid", "h-bot"]), 3, 2),
        Alarm("v-left", True, (2, 3), 2, False, fs(), fs(["h-bot"]), 1),
        Alarm("v-right", True, (2, 12), 3, False, fs(["h-bot"]), fs(["v-bot-right"]), 1),
        Alarm("v-bot-left", True, (4, 6), 2, False, fs(), fs(), 4),
        Alarm("v-bot-right", True, (5, 13), 1, False, fs(), fs(["v-right", "h-bot"])),
        Alarm("h-mid", False, (2, 6), 3, False, fs(), fs(["h-bot", "v-top-left", "v-top-right"])),
        Alarm("h-bot", False, (4, 11), 3, False, fs(["v-right"]), fs(["v-bot-right"]))
    ],
    0x1a: [
        Alarm("v-top-left", True, (0, 5), 2, False, fs(), fs(["h-top", "v-mid-left"]), 3),
        Alarm("v-top-mid", True, (0, 10), 3, False,
              fs(["h-top"]), fs(["v-mid", "v-bot", "v-mid-left"]), 2),
        Alarm("v-top-right", True, (0, 13), 2, False, fs(), fs(["h-top", "v-mid-left"])),
        Alarm("v-mid-left", True, (2, 5), 2, False, fs(), fs(), 2),  # lessened in all others because blocks computer
        Alarm("v-mid", True, (3, 11), 2, False,
              fs(), fs(["v-top-mid", "v-bot", "v-mid-left"]), 1),
        Alarm("v-mid-right", True, (2, 13), 2, True, fs(), fs(["v-mid-left"])),
        Alarm("v-bot-left", True, (4, 3), 2, False, fs(["h-left"]), fs(["v-mid-left"])),
        Alarm("v-bot", True, (5, 12), 1, False, fs(), fs(["v-top-mid", "v-mid", "v-mid-left"])),
        Alarm("h-top", False, (2, 8), 5, False, fs(["v-top-mid"]), fs(["v-top-left", "v-top-right", "v-mid-left"])),
        Alarm("h-left", False, (4, 3), 2, False, fs(["v-bot-left"]), fs(["v-mid-left"])),
    ],
    0x1c: [
        Alarm("v-top-1", True, (0, 5), 3, False, fs(["h-top"]), fs(["v-mid-1", "v-bot-1", "h-mid-1"]), 1),
        Alarm("v-top-2", True, (0, 7), 2, False, fs(["h-top"]), fs(["v-mid-2", "v-bot-2", "h-mid-2"]), 2),
        Alarm("v-top-3", True, (0, 10), 3, False, fs(["h-top"]), fs(["v-bot-3"])),
        Alarm("v-top-4", True, (0, 14), 2, False, fs(["h-top"]), fs()),
        Alarm("v-mid-1", True, (3, 4), 2, False, fs(["h-mid-1"]), fs(["v-top-1", "v-bot-1"]), 1),
        Alarm("v-mid-2", True, (2, 7), 2, True, fs(["h-mid-2"]), fs(["v-top-2", "v-bot-2", "h-top"]), 2, 1),
        #      v-mid-3 is not missing, it's just combined with v-bot-3
        Alarm("v-mid-4", True, (2, 14), 2, False, fs(), fs(["v-bot-3"])),
        Alarm("v-bot-1", True, (5, 6), 1, False, fs(), fs(["v-top-1", "v-mid-1", "h-mid-1"])),
        Alarm("v-bot-2", True, (4, 7), 2, False, fs(), fs(["v-top-2", "h-top", "v-mid-2", "h-mid-2"])),
        Alarm("v-bot-3", True, (3, 10), 3, False, fs(["h-mid-3"]), fs(["v-mid-4"]), 1),
        Alarm("h-top", False, (1, 1), 14, False, fs(["v-top-1", "v-top-2", "v-top-3", "v-top-4"]),
              fs(["v-mid-2", "h-mid-2", "v-bot-2"])),
        Alarm("h-mid-1", False, (4, 2), 5, False, fs(["v-mid-1"]), fs(["v-top-1", "v-bot-1", "h-mid-3"])),
        Alarm("h-mid-2", False, (3, 6), 4, False, fs(["v-mid-2"]), fs(["v-top-2", "h-top", "v-bot-2"])),
        Alarm("h-mid-3", False, (4, 9), 5, False, fs(["v-bot-3"]), fs(["h-mid-1"])),
    ],
    0x21: [
        Alarm("v-mid-left", True, (3, 3), 2, False, fs(), fs(["v-bot-left", "h-bot"])),
        Alarm("v-bot-left", True, (5, 3), 1, False, fs(["h-bot"]), fs(["v-mid-left"])),
        Alarm("v-top-right", True, (0, 13), 2, False, fs(), fs(["h-top", "h-mid"])),
        Alarm("v-mid-right", True, (4, 13), 1, False, fs(), fs(["v-bot-right", "h-bot"])),
        Alarm("v-bot-right", True, (5, 13), 1, False, fs(), fs(["v-mid-right", "h-bot"])),
        Alarm("h-top", False, (2, 9), 4, False, fs(), fs(["v-top-right", "h-mid"])),
        Alarm("h-mid", False, (3, 7), 6, False, fs(), fs(["v-top-right", "h-top"])),
        Alarm("h-bot", False, (5, 3), 9, True, fs(["v-bot-left"]),
              fs(["v-mid-left", "v-mid-right", "v-bot-right"])),
    ],
    0x22: [
        Alarm("v-top-left", True, (0, 2), 2, False, fs(), fs()),
        Alarm("v-mid-left", True, (3, 5), 1, False, fs(["h-mid"]), fs(["v-top-mid", "h-left"])),
        Alarm("v-top-mid", True, (0, 4), 3, False, fs(["h-top"]), fs(["v-mid-left", "h-left"]), 1),
        Alarm("v-top-right", True, (0, 8), 2, False, fs(), fs(), 2),
        Alarm("v-mid-right", True, (3, 12), 1, False, fs(["h-right"]), fs()),
        Alarm("v-bot", True, (4, 7), 2, False, fs(), fs(), 5),
        Alarm("h-top", False, (2, 2), 4, False, fs(["v-top-mid"]), fs()),
        Alarm("h-left", False, (3, 1), 3, False, fs(),
              fs(["v-top-mid", "v-mid-left", "h-mid", "h-right"])),
        Alarm("h-mid", False, (3, 5), 6, True, fs(["v-mid-left"]),
              fs(["h-left", "h-right", "v-top-mid", "v-mid-left", "v-mid-right"])),
        Alarm("h-right", False, (3, 12), 3, False, fs(["v-mid-right"]), fs(["h-left", "h-mid"])),
    ],
    0x24: [
        Alarm("v-top-left", True, (0, 3), 2, False, fs(), fs(), 1),
        Alarm("v-top-right", True, (0, 12), 2, False, fs(), fs(["h-top"])),
        Alarm("v-mid-left", True, (2, 9), 2, False, fs(["h-top"]), fs(["h-bot"])),
        Alarm("v-mid-right", True, (2, 13), 2, False, fs(), fs(["h-bot"])),
        Alarm("v-bot-left", True, (4, 5), 2, False, fs(), fs(), 3),
        Alarm("v-bot-right", True, (4, 13), 2, True, fs(), fs()),
        Alarm("h-top", False, (2, 9), 3, False, fs(["v-mid-left"]), fs(["v-top-right"])),
        Alarm("h-bot", False, (4, 9), 4, False, fs(), fs(["v-mid-left", "v-mid-right"])),
    ],
    0x2d: [
        Alarm("v-top-left", True, (0, 2), 2, False, fs(["h-top"]), fs(["h-mid-left", "v-mid-left"]), 1),
        Alarm("v-mid-left", True, (2, 2), 2, False, fs(), fs(["v-top-left", "h-mid-left", "h-top"])),
        Alarm("h-top", False, (1, 1), 14, False, fs(["v-top-left"]), fs(["v-mid-left"])),
        # h-top makes h-mid-left redundant, but I want path blockers to be less likely
        Alarm("h-mid-left", False, (2, 1), 1, False, fs(), fs(["v-top-left", "v-mid-left"])),
        Alarm("h-mid-right", False, (2, 3), 12, False, fs(), fs(["h-bot-right"])),
        Alarm("h-bot-mid", False, (4, 4), 2, True, fs(), fs(), 1, 0),
        Alarm("h-bot-right", False, (3, 7), 8, False, fs(), fs()),
    ],
    0x2f: [
        Alarm("v-top-left", True, (0, 4), 2, False, fs(), fs()),
        Alarm("v-top-mid", True, (0, 6), 2, True, fs(), fs(["v-mid", "h-top-left", "h-top-right"]), 3, 1),
        Alarm("v-top-right", True, (0, 14), 2, False, fs(), fs()),
        Alarm("v-mid", True, (3, 9), 1, False, fs(), fs(["v-top-mid", "h-top-left", "h-top-right"])),
        Alarm("v-right", True, (2, 12), 2, False, fs(), fs(), 1),
        Alarm("h-top-left", False, (2, 4), 2, False, fs(), fs(["v-top-mid", "v-mid", "h-top-right"])),
        Alarm("h-top-right", False, (2, 9), 3, False, fs(), fs(["v-top-mid", "v-mid", "h-top-left"])),
        Alarm("h-bot-left", False, (4, 1), 3, False, fs(), fs()),
    ],
    0x33: [
        Alarm("v-top", True, (0, 12), 2, False, fs(), fs(["h-right", "h-bot"]), 1),
        Alarm("v-bot", True, (5, 12), 1, False, fs(), fs(["h-bot"])),
        Alarm("h-left", False, (2, 1), 5, True, fs(), fs()),
        Alarm("h-right", False, (2, 13), 2, False, fs(), fs(["v-top", "h-bot"])),
        Alarm("h-bot", False, (4, 9), 4, False, fs(), fs(["v-bot", "v-top", "h-right"])),
    ],
    0x39: [
        Alarm("v-top-left", True, (0, 2), 2, False, fs(), fs(), 1),
        Alarm("v-top-mid", True, (0, 6), 2, False, fs(),
              fs(["v-top-right", "h-top-mid", "v-mid-left", "h-mid", "h-bot"]), 1),
        Alarm("v-top-right", True, (0, 10), 2, False, fs(),
              fs(["h-top-right", "h-mid", "h-bot", "v-mid-left"]), 1),
        Alarm("v-mid-left", True, (2, 5), 2, False, fs(),
              fs(["v-top-mid", "v-top-right", "h-top-right", "h-top-mid"])),
        Alarm("v-mid-right", True, (2, 13), 2, False, fs(), fs(["v-bot-right", "h-bot", "h-mid"])),
        Alarm("v-bot-left", True, (5, 4), 1, False, fs(["h-bot"]), fs(["h-mid", "v-mid-left", "v-top-mid"])),
        Alarm("v-bot-right", True, (5, 13), 1, False, fs(), fs(["v-mid-right"])),
        Alarm("h-top-mid", False, (2, 7), 1, False, fs(),
              fs(["h-top-right", "v-top-right", "v-top-mid", "v-mid-left"])),
        Alarm("h-top-right", False, (2, 11), 2, False, fs(), fs(["v-top-right"])),
        Alarm("h-mid", False, (4, 5), 6, False, fs(), fs(["h-bot", "v-mid-right", "v-bot-left", "v-bot-right"])),
        Alarm("h-bot", False, (5, 4), 8, True, fs(["v-bot-left"]), fs(["h-mid", "v-mid-right", "v-bot-right"])),
    ],
    0x3b: [
        Alarm("v-top", True, (0, 11), 2, False, fs(), fs(["v-bot", "h-top-left", "h-mid-left"])),
        Alarm("v-bot", True, (5, 11), 1, False, fs(), fs(["v-top", "h-top-left", "h-mid-left"])),
        Alarm("h-top-left", False, (2, 1), 4, False, fs(), fs(["h-mid-left", "v-top", "v-bot"])),
        Alarm("h-mid-left", False, (3, 1), 2, False, fs(), fs(["h-top-left", "v-top", "v-bot"])),
        Alarm("h-top-mid", False, (2, 7), 2, False, fs(), fs(["h-mid"])),
        Alarm("h-mid", False, (3, 6), 4, True, fs(), fs(["h-top-mid"])),
    ],
    0x3d: [
        Alarm("v-top", True, (0, 9), 2, False, fs(), fs(), 4),
        Alarm("v-mid-left", True, (2, 2), 2, False, fs(), fs(["v-mid-right", "h-right"]), 4),
        Alarm("v-mid-right", True, (3, 10), 1, False, fs(["h-right"]), fs(["v-bot", "v-mid-left"])),
        Alarm("v-bot", True, (4, 9), 2, False, fs(), fs(["v-mid-right", "h-right"]), 4),
        Alarm("h-right", False, (3, 10), 5, True, fs(["v-mid-right"]), fs(["v-bot", "v-mid-left"])),
    ],
    0x3f: [
        Alarm("v-top", True, (0, 2), 2, False, fs(), fs()),
        Alarm("v-bot", True, (4, 7), 2, True, fs(), fs(["h-bot-left", "h-bot-right"])),
        Alarm("h-top-right", False, (2, 8), 4, False, fs(), fs()),
        Alarm("h-right", False, (3, 11), 4, False, fs(), fs()),
        Alarm("h-bot-left", False, (4, 5), 2, False, fs(), fs(["v-bot", "h-bot-right"])),
        Alarm("h-bot-right", False, (4, 8), 2, False, fs(), fs(["v-bot", "h-bot-left"])),
    ],
}
""" map_index: list of possible `Alarm` in room """
