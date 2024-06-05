from typing import Mapping


item_room_codes: Mapping[int, int] = {
    0x0a: 0x00,
    0x0b: 0x02,
    0x0d: 0x04,
    0x0f: 0x06,
    0x10: 0x08,
    0x17: 0x0a,
    0x1a: 0x0c,
    0x1b: 0x0e,
    0x1c: 0x10,
    0x1d: 0x12,
    0x21: 0x14,
    0x22: 0x16,
    0x24: 0x18,
    0x25: 0x1a,
    0x29: 0x1c,
    0x2b: 0x1e,
    0x2c: 0x20,
    0x2d: 0x22,
    0x2f: 0x24,
    0x31: 0x26,
    0x33: 0x28,
    0x34: 0x2a,
    0x36: 0x2c,
    0x37: 0x2e,
    0x39: 0x30,
    0x3b: 0x32,
    0x3c: 0x34,
    0x3d: 0x36,
    0x3e: 0x38,
    0x3f: 0x3a,
    0x43: 0x3c,
    0x44: 0x3e,
    0x45: 0x40,
    0x46: 0x42,
    0x47: 0x44,
    0x49: 0x46,
    0x4b: 0x48,
    0x4c: 0x4a,
    0x4d: 0x4c,
    0x4f: 0x4e,
    0x51: 0x50,
    0x52: 0x52,
    0x53: 0x54,
    0x54: 0x56,
    0x59: 0x58,
    0x5a: 0x5a,
    0x5b: 0x5c,
    0x5c: 0x5e,
    0x5d: 0x60,
    0x5e: 0x62,
    0x61: 0x64,
    0x62: 0x66,
    0x63: 0x68,
    0x64: 0x6a,
    0x65: 0x6c,
    0x66: 0x6e,
    0x69: 0x70,
    0x6a: 0x72,
    0x6b: 0x74,
    0x6c: 0x76,
    0x6d: 0x78,
    0x6e: 0x7a,
    0x71: 0x7c,
    0x72: 0x7e,
    0x73: 0x80,
    0x74: 0x82,
    0x75: 0x84,
    0x76: 0x86,
    0x7a: 0x88,
    0x7b: 0x8a,
    0x7c: 0x8c,
    0x7d: 0x8e,
    0x7e: 0x90,
    0x82: 0x92,
}
"""
map index to item room code

item room code == 2 * item room index
"""