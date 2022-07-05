from typing import Dict
from zilliandomizer.room_gen.common import RoomData, TOP_LEFT, TOP_RIGHT, BOT_LEFT, BOT_RIGHT

GEN_ROOMS: Dict[int, RoomData] = {
    0x0a: RoomData([BOT_LEFT, TOP_RIGHT], True),
    0x0b: RoomData([TOP_LEFT, BOT_RIGHT], False),
    # 0x0d: RoomData([_BOT_LEFT, (1, 9), (1, 10)]),
    0x0f: RoomData([BOT_LEFT], False),

    0x10: RoomData([BOT_RIGHT], False),
    0x17: RoomData([BOT_LEFT, TOP_LEFT], True),

    0x1a: RoomData([BOT_RIGHT, BOT_LEFT, (5, 5)], True),
    0x1b: RoomData([BOT_RIGHT, BOT_LEFT], True),
    0x1c: RoomData([BOT_RIGHT, BOT_LEFT], True),
    0x1d: RoomData([BOT_RIGHT, BOT_LEFT], True),

    0x21: RoomData([BOT_LEFT, BOT_RIGHT], True),
    0x22: RoomData([BOT_LEFT, BOT_RIGHT, (1, 5)], True),
    0x24: RoomData([BOT_LEFT, TOP_RIGHT], True),
    0x25: RoomData([TOP_LEFT, BOT_RIGHT], True),

    0x29: RoomData([BOT_RIGHT, BOT_LEFT, (5, 7)], True),
    0x2b: RoomData([(5, 1), BOT_RIGHT], True),
    # 0x2c: RoomData([_BOT_LEFT, _TOP_RIGHT, (1, 11)]),
    0x2d: RoomData([BOT_RIGHT], False),
    0x2f: RoomData([BOT_LEFT, BOT_RIGHT], True),

    0x31: RoomData([(1, 7), BOT_RIGHT], True),
    0x33: RoomData([BOT_RIGHT, BOT_LEFT, (1, 1)], True),
    0x34: RoomData([BOT_RIGHT, BOT_LEFT], True),
    0x36: RoomData([BOT_RIGHT, BOT_LEFT], True),  # 2 in bot right
    0x37: RoomData([TOP_RIGHT, BOT_LEFT], True),
}
