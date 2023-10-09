from typing import Dict, List

from .terrain_compressor import TerrainCompressor
from . import rom_info


terrain_mods = {
    0x0a: [
        0x81, 0x30, 0x0f, 0x3a, 0x81, 0x30, 0x03, 0x39, 0x0c, 0x3b, 0x84,
        0x30, 0x3b, 0x39, 0x39, 0x0b, 0x3a, 0x02, 0x30, 0x81, 0x3c, 0x09,
        0x3b, 0x04, 0x39, 0x81, 0x30, 0x0b, 0x3a, 0x02, 0x39, 0x83, 0x3b,
        0x39, 0x30, 0x0d, 0x3b, 0x83, 0x3c, 0x3b, 0x30, 0x00,
    ],
    0x0b: [
        0x0f, 0x3a, 0x83, 0x30, 0x3b, 0x3b, 0x0d, 0x39, 0x02, 0x30, 0x85,
        0x3a, 0x39, 0x39, 0x3b, 0x3b, 0x09, 0x39, 0x02, 0x30, 0x03, 0x39,
        0x86, 0x3a, 0x40, 0x39, 0x39, 0x3b, 0x3b, 0x05, 0x39, 0x02, 0x30,
        0x04, 0x39, 0x8c, 0x3f, 0x39, 0x39, 0x3a, 0x3a, 0x39, 0x3b, 0x3b,
        0x39, 0x39, 0x3a, 0x30, 0x04, 0x3b, 0x81, 0x41, 0x05, 0x3b, 0x02,
        0x3c, 0x03, 0x3b, 0x00,
    ],
    0x0d: [
        0x81, 0x30, 0x04, 0x3a, 0x02, 0x44, 0x08, 0x3a, 0x02, 0x30, 0x09,
        0x39, 0x03, 0x3b, 0x02, 0x39, 0x02, 0x30, 0x81, 0x3b, 0x03, 0x39,
        0x82, 0x3b, 0x32, 0x03, 0x39, 0x03, 0x3a, 0x02, 0x39, 0x02, 0x30,
        0x81, 0x3c, 0x03, 0x3b, 0x83, 0x3c, 0x36, 0x3b, 0x06, 0x39, 0x82,
        0x3b, 0x30, 0x08, 0x3a, 0x02, 0x39, 0x02, 0x3b, 0x02, 0x39, 0x82,
        0x3a, 0x30, 0x0a, 0x3b, 0x02, 0x3c, 0x03, 0x3b, 0x81, 0x30, 0x00,
    ],
    0x0f: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x02, 0x3b, 0x07, 0x39, 0x81,
        0x3b, 0x04, 0x39, 0x02, 0x30, 0x82, 0x3a, 0x40, 0x05, 0x39, 0x02,
        0x3b, 0x82, 0x37, 0x3b, 0x03, 0x39, 0x02, 0x30, 0x82, 0x3b, 0x41,
        0x03, 0x39, 0x02, 0x3b, 0x81, 0x30, 0x03, 0x3a, 0x02, 0x39, 0x8b,
        0x3b, 0x30, 0x30, 0x3a, 0x3a, 0x39, 0x3b, 0x3b, 0x30, 0x3a, 0x3a,
        0x03, 0x39, 0x85, 0x3b, 0x39, 0x3a, 0x30, 0x30, 0x03, 0x3b, 0x83,
        0x30, 0x3c, 0x3c, 0x05, 0x3b, 0x84, 0x3c, 0x3b, 0x3b, 0x30, 0x00,
    ],
    0x10: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x06, 0x39, 0x08, 0x3b, 0x02,
        0x30, 0x02, 0x39, 0x02, 0x3b, 0x02, 0x39, 0x08, 0x3a, 0x02, 0x30,
        0x86, 0x3b, 0x39, 0x3a, 0x3a, 0x3b, 0x3b, 0x05, 0x39, 0x03, 0x3b,
        0x02, 0x30, 0x81, 0x3a, 0x03, 0x39, 0x83, 0x3a, 0x33, 0x3b, 0x04,
        0x39, 0x04, 0x3a, 0x81, 0x30, 0x05, 0x3b, 0x82, 0x35, 0x3c, 0x08,
        0x3b, 0x00,
    ],
    0x17: [
        0x81, 0x30, 0x0a, 0x3a, 0x81, 0x40, 0x03, 0x3a, 0x02, 0x30, 0x05,
        0x3b, 0x03, 0x39, 0x02, 0x3b, 0x81, 0x41, 0x03, 0x3b, 0x02, 0x30,
        0x04, 0x3a, 0x84, 0x3c, 0x3b, 0x3b, 0x39, 0x06, 0x3a, 0x02, 0x30,
        0x04, 0x3b, 0x03, 0x3c, 0x03, 0x3b, 0x03, 0x39, 0x82, 0x3b, 0x30,
        0x0b, 0x3a, 0x85, 0x39, 0x3b, 0x39, 0x3a, 0x30, 0x0c, 0x3b, 0x84,
        0x3c, 0x3b, 0x3b, 0x30, 0x00,
    ],
    0x1a: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x07, 0x3b, 0x05, 0x39, 0x02,
        0x3b, 0x02, 0x30, 0x07, 0x3a, 0x02, 0x39, 0x02, 0x3b, 0x89, 0x39,
        0x40, 0x3a, 0x30, 0x30, 0x3b, 0x3b, 0x39, 0x39, 0x03, 0x3b, 0x02,
        0x39, 0x02, 0x3a, 0x84, 0x39, 0x41, 0x3b, 0x30, 0x03, 0x3a, 0x02,
        0x39, 0x88, 0x30, 0x3a, 0x3a, 0x39, 0x39, 0x3b, 0x3b, 0x39, 0x03,
        0x3a, 0x05, 0x3b, 0x81, 0x30, 0x04, 0x3b, 0x02, 0x3c, 0x04, 0x3b,
        0x00,
    ],
    0x1b: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x03, 0x39, 0x0b, 0x3b, 0x02,
        0x30, 0x83, 0x3b, 0x39, 0x39, 0x0b, 0x3a, 0x02, 0x30, 0x81, 0x3c,
        0x06, 0x3b, 0x02, 0x3e, 0x05, 0x39, 0x81, 0x30, 0x0a, 0x3a, 0x86,
        0x39, 0x3b, 0x3b, 0x39, 0x39, 0x3a, 0x0b, 0x3b, 0x02, 0x3c, 0x03,
        0x3b, 0x00,
    ],
    0x1c: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x06, 0x39, 0x02, 0x3b, 0x05,
        0x39, 0x83, 0x3b, 0x30, 0x30, 0x03, 0x39, 0x02, 0x3b, 0xa3, 0x39,
        0x3a, 0x40, 0x39, 0x3b, 0x3b, 0x39, 0x39, 0x3a, 0x30, 0x30, 0x3b,
        0x39, 0x39, 0x3a, 0x3a, 0x39, 0x3b, 0x41, 0x39, 0x3a, 0x3a, 0x39,
        0x39, 0x3b, 0x30, 0x3a, 0x3a, 0x39, 0x39, 0x3b, 0x3b, 0x39, 0x3a,
        0x3a, 0x05, 0x39, 0x02, 0x3a, 0x04, 0x3b, 0x02, 0x3c, 0x0a, 0x3b,
        0x00,
    ],
    0x1d: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x06, 0x39, 0x08, 0x3b, 0x02,
        0x30, 0x02, 0x39, 0x02, 0x3b, 0x02, 0x39, 0x08, 0x3a, 0x02, 0x30,
        0x84, 0x3b, 0x39, 0x3a, 0x3a, 0x03, 0x3b, 0x04, 0x39, 0x03, 0x3b,
        0x83, 0x30, 0x3a, 0x3a, 0x03, 0x39, 0x02, 0x3a, 0x85, 0x30, 0x3b,
        0x3b, 0x39, 0x39, 0x04, 0x3a, 0x07, 0x3b, 0x83, 0x30, 0x3c, 0x3c,
        0x06, 0x3b, 0x00,
    ],
    0x21: [
        0x81, 0x30, 0x05, 0x3a, 0x81, 0x33, 0x08, 0x3a, 0x02, 0x30, 0x04,
        0x39, 0x84, 0x3b, 0x35, 0x3b, 0x3b, 0x06, 0x39, 0x02, 0x30, 0x02,
        0x3b, 0x02, 0x39, 0x84, 0x3a, 0x33, 0x3a, 0x3a, 0x04, 0x39, 0x8a,
        0x32, 0x39, 0x30, 0x30, 0x3a, 0x3a, 0x39, 0x39, 0x3b, 0x35, 0x06,
        0x39, 0x84, 0x36, 0x3b, 0x30, 0x3a, 0x04, 0x39, 0x84, 0x3a, 0x33,
        0x3b, 0x3b, 0x04, 0x39, 0x03, 0x3a, 0x02, 0x3b, 0x81, 0x45, 0x09,
        0x43, 0x81, 0x45, 0x03, 0x3b, 0x00,
    ],
    0x22: [
        0x81, 0x30, 0x0e, 0x3a, 0x02, 0x30, 0x81, 0x3b, 0x04, 0x39, 0x09,
        0x3b, 0x02, 0x30, 0x81, 0x3a, 0x04, 0x39, 0x09, 0x3a, 0x02, 0x30,
        0x03, 0x3b, 0x81, 0x45, 0x06, 0x43, 0x85, 0x45, 0x3b, 0x39, 0x39,
        0x30, 0x0d, 0x3a, 0x02, 0x39, 0x81, 0x3a, 0x10, 0x3b, 0x00,
    ],
    0x24: [
        0x81, 0x30, 0x07, 0x3a, 0x81, 0x33, 0x07, 0x3a, 0x81, 0x30, 0x03,
        0x3b, 0x02, 0x39, 0x02, 0x3e, 0x81, 0x35, 0x03, 0x39, 0x04, 0x3b,
        0x81, 0x30, 0x03, 0x3a, 0x02, 0x39, 0x83, 0x34, 0x3a, 0x3a, 0x03,
        0x39, 0x03, 0x3a, 0x02, 0x30, 0x02, 0x3b, 0x02, 0x39, 0x84, 0x3b,
        0x36, 0x3b, 0x3b, 0x04, 0x39, 0x02, 0x3b, 0x81, 0x30, 0x03, 0x3a,
        0x02, 0x39, 0x04, 0x3a, 0x04, 0x39, 0x83, 0x40, 0x3a, 0x30, 0x0d,
        0x3b, 0x83, 0x41, 0x3b, 0x30, 0x00,
    ],
    0x25: [
        0x0f, 0x3a, 0x81, 0x30, 0x03, 0x3b, 0x03, 0x39, 0x02, 0x3b, 0x02,
        0x39, 0x02, 0x3b, 0x02, 0x39, 0x85, 0x3b, 0x30, 0x30, 0x3a, 0x3a,
        0x03, 0x39, 0x02, 0x3a, 0x02, 0x39, 0x02, 0x3a, 0x02, 0x39, 0x86,
        0x3a, 0x30, 0x30, 0x3b, 0x39, 0x39, 0x0b, 0x3b, 0x02, 0x30, 0x83,
        0x3a, 0x39, 0x39, 0x0c, 0x3a, 0x81, 0x30, 0x0f, 0x3b, 0x00,
    ],
    0x29: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x03, 0x0f, 0x03, 0x13, 0x02,
        0x0f, 0x81, 0x13, 0x05, 0x0f, 0x02, 0x01, 0x03, 0x0e, 0x86, 0x07,
        0x10, 0x10, 0x0e, 0x0e, 0x06, 0x05, 0x0e, 0x02, 0x01, 0x02, 0x13,
        0x83, 0x0f, 0x05, 0x0f, 0x03, 0x13, 0x87, 0x0d, 0x0f, 0x13, 0x13,
        0x0f, 0x0f, 0x01, 0x03, 0x10, 0x83, 0x0e, 0x03, 0x0e, 0x03, 0x10,
        0x87, 0x06, 0x0e, 0x10, 0x10, 0x0e, 0x0e, 0x10, 0x04, 0x13, 0x81,
        0x0c, 0x04, 0x13, 0x81, 0x0d, 0x06, 0x13, 0x00,
    ],
    0x2b: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x81, 0x13, 0x0d, 0x0f, 0x02,
        0x01, 0x81, 0x10, 0x06, 0x0e, 0x83, 0x12, 0x0b, 0x12, 0x04, 0x0e,
        0x02, 0x01, 0x81, 0x13, 0x04, 0x0f, 0x02, 0x13, 0x83, 0x21, 0x11,
        0x11, 0x03, 0x0f, 0x8b, 0x13, 0x01, 0x01, 0x10, 0x0e, 0x0e, 0x12,
        0x12, 0x1e, 0x10, 0x10, 0x03, 0x0e, 0x85, 0x12, 0x0e, 0x10, 0x10,
        0x01, 0x03, 0x13, 0x83, 0x20, 0x15, 0x15, 0x05, 0x13, 0x81, 0x15,
        0x03, 0x13, 0x00,
    ],
    0x2c: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x04, 0x0f, 0x0a, 0x13, 0x02,
        0x01, 0x81, 0x12, 0x03, 0x0e, 0x0a, 0x10, 0x02, 0x01, 0x81, 0x15,
        0x06, 0x13, 0x02, 0x17, 0x05, 0x0f, 0x81, 0x01, 0x0a, 0x10, 0x86,
        0x0e, 0x12, 0x12, 0x0e, 0x0e, 0x01, 0x0b, 0x13, 0x02, 0x15, 0x02,
        0x13, 0x81, 0x01, 0x00,
    ],
    0x2d: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x82, 0x0f, 0x13, 0x0c, 0x0f,
        0x02, 0x01, 0x82, 0x0e, 0x10, 0x03, 0x0e, 0x81, 0x12, 0x08, 0x0e,
        0x02, 0x01, 0x81, 0x13, 0x04, 0x0f, 0x81, 0x09, 0x08, 0x0f, 0x02,
        0x01, 0x86, 0x10, 0x0e, 0x02, 0x1b, 0x1b, 0x03, 0x08, 0x0e, 0x88,
        0x10, 0x01, 0x13, 0x13, 0x0d, 0x13, 0x13, 0x0c, 0x09, 0x13, 0x00,
    ],
    0x2f: [
        0x81, 0x01, 0x06, 0x10, 0x81, 0x18, 0x07, 0x10, 0x02, 0x01, 0x03,
        0x13, 0x02, 0x0f, 0x83, 0x13, 0x19, 0x13, 0x03, 0x0f, 0x03, 0x13,
        0x02, 0x01, 0x03, 0x10, 0x02, 0x0e, 0x03, 0x14, 0x03, 0x0e, 0x03,
        0x10, 0x02, 0x01, 0x03, 0x0f, 0x02, 0x13, 0x03, 0x15, 0x04, 0x13,
        0x02, 0x0f, 0x82, 0x01, 0x10, 0x03, 0x0e, 0x06, 0x10, 0x86, 0x07,
        0x10, 0x10, 0x0e, 0x0e, 0x01, 0x0a, 0x13, 0x81, 0x0c, 0x04, 0x13,
        0x81, 0x01, 0x00,
    ],
    0x31: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x0c, 0x13, 0x02, 0x0f, 0x02,
        0x01, 0x0c, 0x10, 0x02, 0x0e, 0x02, 0x01, 0x81, 0x0f, 0x03, 0x16,
        0x81, 0x0f, 0x04, 0x16, 0x8d, 0x0f, 0x13, 0x13, 0x0f, 0x0f, 0x01,
        0x01, 0x0e, 0x07, 0x10, 0x10, 0x0e, 0x07, 0x03, 0x10, 0x89, 0x0e,
        0x07, 0x10, 0x0e, 0x0e, 0x01, 0x01, 0x13, 0x0c, 0x03, 0x13, 0x81,
        0x0c, 0x04, 0x13, 0x81, 0x0c, 0x03, 0x13, 0x81, 0x01, 0x00,
    ],
    0x33: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x09, 0x0f, 0x03, 0x13, 0x02,
        0x0f, 0x02, 0x01, 0x05, 0x1b, 0x81, 0x03, 0x03, 0x0e, 0x03, 0x10,
        0x02, 0x0e, 0x02, 0x01, 0x81, 0x24, 0x03, 0x13, 0x84, 0x24, 0x0c,
        0x13, 0x13, 0x04, 0x0f, 0x02, 0x13, 0x81, 0x01, 0x09, 0x10, 0x02,
        0x0e, 0x82, 0x12, 0x0e, 0x03, 0x10, 0x0b, 0x13, 0x81, 0x15, 0x04,
        0x13, 0x00,
    ],
    0x34: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x07, 0x0f, 0x07, 0x13, 0x02,
        0x01, 0x02, 0x0e, 0x02, 0x12, 0x03, 0x0e, 0x07, 0x10, 0x02, 0x01,
        0x87, 0x13, 0x0f, 0x11, 0x11, 0x0f, 0x13, 0x13, 0x04, 0x0f, 0x03,
        0x13, 0x83, 0x01, 0x10, 0x10, 0x04, 0x0e, 0x86, 0x10, 0x06, 0x12,
        0x12, 0x0e, 0x0e, 0x04, 0x10, 0x07, 0x13, 0x83, 0x0d, 0x15, 0x15,
        0x06, 0x13, 0x00,
    ],
    0x36: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x02, 0x13, 0x03, 0x0f, 0x04,
        0x13, 0x03, 0x0f, 0x02, 0x13, 0x02, 0x01, 0x02, 0x10, 0x03, 0x0e,
        0x04, 0x10, 0x03, 0x0e, 0x02, 0x10, 0x02, 0x01, 0x03, 0x13, 0x08,
        0x0f, 0x03, 0x13, 0x81, 0x01, 0x03, 0x10, 0x81, 0x1e, 0x06, 0x12,
        0x02, 0x0e, 0x04, 0x10, 0x03, 0x13, 0x07, 0x15, 0x06, 0x13, 0x00,
    ],
    0x37: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x81, 0x0f, 0x0d, 0x13, 0x02,
        0x01, 0x81, 0x0e, 0x0d, 0x10, 0x02, 0x01, 0x0d, 0x13, 0x82, 0x0f,
        0x01, 0x0e, 0x10, 0x82, 0x0e, 0x01, 0x0f, 0x13, 0x81, 0x01, 0x00,
    ],
    0x39: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x02, 0x13, 0x02, 0x0f, 0x02,
        0x13, 0x81, 0x0f, 0x03, 0x13, 0x03, 0x0f, 0x8a, 0x13, 0x01, 0x01,
        0x10, 0x10, 0x0e, 0x0e, 0x10, 0x10, 0x0e, 0x03, 0x10, 0x02, 0x0e,
        0x02, 0x10, 0x02, 0x01, 0x81, 0x0f, 0x03, 0x13, 0x06, 0x0f, 0x02,
        0x17, 0x02, 0x0f, 0x86, 0x01, 0x10, 0x0e, 0x10, 0x1e, 0x10, 0x06,
        0x0e, 0x85, 0x10, 0x1f, 0x0e, 0x0e, 0x01, 0x03, 0x13, 0x81, 0x24,
        0x08, 0x22, 0x84, 0x24, 0x13, 0x13, 0x01, 0x00,
    ],
    0x3b: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x04, 0x0f, 0x02, 0x16, 0x02,
        0x0f, 0x02, 0x17, 0x04, 0x0f, 0x02, 0x01, 0x02, 0x0e, 0x02, 0x12,
        0x91, 0x01, 0x10, 0x0e, 0x0e, 0x10, 0x01, 0x12, 0x12, 0x0e, 0x0e,
        0x01, 0x01, 0x0f, 0x0f, 0x20, 0x25, 0x25, 0x04, 0x22, 0x02, 0x25,
        0x8a, 0x21, 0x0f, 0x0f, 0x01, 0x01, 0x12, 0x0e, 0x10, 0x10, 0x01,
        0x04, 0x14, 0x88, 0x01, 0x10, 0x10, 0x0e, 0x0e, 0x10, 0x01, 0x15,
        0x03, 0x13, 0x06, 0x15, 0x05, 0x13, 0x00,
    ],
    0x3c: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x06, 0x13, 0x02, 0x0f, 0x06,
        0x13, 0x02, 0x01, 0x06, 0x10, 0x02, 0x0e, 0x06, 0x10, 0x02, 0x01,
        0x81, 0x0f, 0x07, 0x13, 0x81, 0x24, 0x04, 0x13, 0x84, 0x0f, 0x01,
        0x10, 0x0e, 0x0c, 0x10, 0x82, 0x0e, 0x10, 0x10, 0x13, 0x00,
    ],
    0x3d: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x06, 0x13, 0x02, 0x0f, 0x06,
        0x13, 0x02, 0x01, 0x06, 0x10, 0x02, 0x0e, 0x06, 0x10, 0x02, 0x01,
        0x81, 0x0f, 0x07, 0x13, 0x81, 0x24, 0x04, 0x22, 0x84, 0x1c, 0x01,
        0x10, 0x0e, 0x0c, 0x10, 0x82, 0x0e, 0x10, 0x10, 0x13, 0x00,
    ],
    0x3e: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x02, 0x16, 0x02, 0x0f, 0x02,
        0x17, 0x85, 0x0f, 0x13, 0x13, 0x0f, 0x0f, 0x03, 0x13, 0x02, 0x01,
        0x02, 0x10, 0x02, 0x0e, 0x02, 0x10, 0x85, 0x0e, 0x10, 0x10, 0x0e,
        0x0e, 0x03, 0x10, 0x02, 0x01, 0x02, 0x0f, 0x02, 0x16, 0x02, 0x0f,
        0x02, 0x13, 0x94, 0x0f, 0x13, 0x13, 0x0f, 0x13, 0x13, 0x01, 0x10,
        0x0e, 0x0e, 0x10, 0x10, 0x0e, 0x0e, 0x10, 0x10, 0x0e, 0x10, 0x10,
        0x0e, 0x03, 0x10, 0x10, 0x13, 0x00,
    ],
    0x3f: [
        0x81, 0x01, 0x06, 0x10, 0x81, 0x01, 0x07, 0x10, 0x02, 0x01, 0x81,
        0x13, 0x05, 0x0f, 0x81, 0x01, 0x04, 0x0f, 0x03, 0x13, 0x02, 0x01,
        0x8b, 0x10, 0x0e, 0x0e, 0x12, 0x0e, 0x0e, 0x23, 0x0e, 0x0e, 0x12,
        0x0e, 0x03, 0x10, 0x02, 0x01, 0x03, 0x0f, 0x87, 0x08, 0x0f, 0x0f,
        0x13, 0x0f, 0x0f, 0x09, 0x04, 0x0f, 0x82, 0x01, 0x10, 0x03, 0x0e,
        0x87, 0x02, 0x0e, 0x0e, 0x18, 0x0e, 0x0e, 0x03, 0x04, 0x0e, 0x81,
        0x01, 0x04, 0x13, 0x87, 0x0d, 0x13, 0x13, 0x19, 0x13, 0x13, 0x0c,
        0x04, 0x13, 0x81, 0x01, 0x00,
    ],
    0x41: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x03, 0x13, 0x81, 0x24, 0x06,
        0x22, 0x86, 0x24, 0x13, 0x0f, 0x0f, 0x01, 0x01, 0x0c, 0x10, 0x02,
        0x0e, 0x02, 0x01, 0x84, 0x0f, 0x13, 0x13, 0x24, 0x06, 0x22, 0x81,
        0x24, 0x03, 0x13, 0x02, 0x01, 0x81, 0x0e, 0x0d, 0x10, 0x02, 0x01,
        0x03, 0x13, 0x81, 0x24, 0x06, 0x22, 0x81, 0x24, 0x03, 0x13, 0x81,
        0x01, 0x00,
    ],
    0x43: [
        0x81, 0x01, 0x0a, 0x10, 0x81, 0x18, 0x03, 0x10, 0x02, 0x01, 0x07,
        0x13, 0x03, 0x0f, 0x81, 0x19, 0x03, 0x13, 0x02, 0x01, 0x07, 0x10,
        0x03, 0x0e, 0x81, 0x01, 0x03, 0x10, 0x02, 0x01, 0x09, 0x0f, 0x87,
        0x01, 0x11, 0x0f, 0x0f, 0x13, 0x01, 0x10, 0x06, 0x0e, 0x02, 0x12,
        0x82, 0x01, 0x10, 0x03, 0x0e, 0x02, 0x10, 0x07, 0x13, 0x03, 0x15,
        0x81, 0x19, 0x05, 0x13, 0x00,
    ],
    0x44: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x07, 0x13, 0x06, 0x0f, 0x83,
        0x13, 0x01, 0x01, 0x07, 0x10, 0x06, 0x0e, 0x83, 0x10, 0x01, 0x01,
        0x08, 0x13, 0x05, 0x0f, 0x82, 0x13, 0x01, 0x05, 0x10, 0x81, 0x01,
        0x03, 0x10, 0x02, 0x0e, 0x85, 0x12, 0x0e, 0x0e, 0x10, 0x10, 0x04,
        0x13, 0x82, 0x24, 0x01, 0x05, 0x13, 0x81, 0x15, 0x04, 0x13, 0x00,
    ],
    0x45: [
        0x81, 0x01, 0x0f, 0x10, 0x83, 0x01, 0x13, 0x13, 0x0c, 0x0f, 0x92,
        0x13, 0x01, 0x10, 0x10, 0x0e, 0x0e, 0x23, 0x1b, 0x1b, 0x23, 0x23,
        0x1b, 0x1b, 0x23, 0x1b, 0x1b, 0x01, 0x01, 0x03, 0x0f, 0x02, 0x13,
        0x04, 0x0f, 0x02, 0x13, 0x03, 0x0f, 0x82, 0x01, 0x10, 0x03, 0x0e,
        0x02, 0x10, 0x86, 0x0e, 0x12, 0x12, 0x0e, 0x10, 0x10, 0x03, 0x0e,
        0x81, 0x01, 0x07, 0x13, 0x02, 0x15, 0x06, 0x13, 0x81, 0x01, 0x00,
    ],
    0x46: [
        0x0f, 0x10, 0x83, 0x01, 0x13, 0x13, 0x0d, 0x0f, 0x02, 0x01, 0x84,
        0x10, 0x0e, 0x12, 0x12, 0x0a, 0x0e, 0x02, 0x01, 0x02, 0x0f, 0x02,
        0x11, 0x02, 0x0f, 0x02, 0x13, 0x06, 0x0f, 0x02, 0x01, 0x06, 0x0e,
        0x02, 0x10, 0x03, 0x0e, 0x85, 0x12, 0x0e, 0x0e, 0x10, 0x01, 0x0b,
        0x13, 0x81, 0x15, 0x03, 0x13, 0x00,
    ],
    0x47: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x81, 0x13, 0x03, 0x17, 0x04,
        0x16, 0x02, 0x13, 0x02, 0x0f, 0x02, 0x13, 0x02, 0x01, 0x0a, 0x10,
        0x02, 0x0e, 0x02, 0x10, 0x02, 0x01, 0x02, 0x13, 0x02, 0x0f, 0x04,
        0x16, 0x06, 0x13, 0x86, 0x01, 0x10, 0x10, 0x01, 0x12, 0x0e, 0x0a,
        0x10, 0x86, 0x01, 0x13, 0x13, 0x15, 0x15, 0x13, 0x03, 0x16, 0x81,
        0x13, 0x03, 0x17, 0x03, 0x13, 0x81, 0x01, 0x00,
    ],
    0x49: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x06, 0x0f, 0x02, 0x13, 0x02,
        0x0f, 0x04, 0x13, 0x02, 0x01, 0x04, 0x0e, 0x02, 0x12, 0x85, 0x01,
        0x10, 0x0e, 0x0e, 0x01, 0x03, 0x10, 0x02, 0x01, 0x02, 0x0f, 0x02,
        0x13, 0x91, 0x01, 0x11, 0x11, 0x0f, 0x13, 0x13, 0x01, 0x0f, 0x0f,
        0x13, 0x01, 0x01, 0x12, 0x12, 0x01, 0x10, 0x10, 0x03, 0x0e, 0x83,
        0x01, 0x10, 0x10, 0x03, 0x0e, 0x02, 0x01, 0x03, 0x15, 0x03, 0x13,
        0x03, 0x24, 0x05, 0x13, 0x81, 0x01, 0x00,
    ],
    0x4b: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x81, 0x13, 0x09, 0x0f, 0x87,
        0x13, 0x0f, 0x0f, 0x13, 0x01, 0x01, 0x10, 0x03, 0x0e, 0x91, 0x23,
        0x1b, 0x1b, 0x23, 0x0e, 0x0e, 0x06, 0x0e, 0x0e, 0x10, 0x01, 0x01,
        0x13, 0x0f, 0x01, 0x13, 0x13, 0x05, 0x0f, 0x81, 0x04, 0x03, 0x0f,
        0x89, 0x01, 0x10, 0x10, 0x0e, 0x10, 0x10, 0x01, 0x12, 0x12, 0x03,
        0x0e, 0x85, 0x02, 0x12, 0x0e, 0x0e, 0x10, 0x05, 0x13, 0x02, 0x15,
        0x81, 0x01, 0x03, 0x13, 0x82, 0x0d, 0x15, 0x03, 0x13, 0x00,
    ],
    0x4c: [
        0x81, 0x01, 0x03, 0x10, 0x81, 0x06, 0x04, 0x10, 0x81, 0x06, 0x05,
        0x10, 0x02, 0x01, 0x03, 0x0f, 0x81, 0x04, 0x04, 0x0f, 0x81, 0x04,
        0x04, 0x0f, 0x83, 0x13, 0x01, 0x01, 0x03, 0x0e, 0x81, 0x02, 0x04,
        0x0e, 0x81, 0x02, 0x04, 0x0e, 0x95, 0x10, 0x01, 0x01, 0x0f, 0x0f,
        0x13, 0x0d, 0x13, 0x0f, 0x0f, 0x13, 0x0d, 0x13, 0x0f, 0x0f, 0x13,
        0x13, 0x01, 0x10, 0x0e, 0x0e, 0x03, 0x10, 0x02, 0x0e, 0x03, 0x10,
        0x02, 0x0e, 0x03, 0x10, 0x10, 0x13, 0x00,
    ],
    0x4d: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x81, 0x13, 0x0d, 0x0f, 0x02,
        0x01, 0x9f, 0x23, 0x1b, 0x01, 0x1b, 0x1b, 0x01, 0x0e, 0x0e, 0x01,
        0x0e, 0x0e, 0x01, 0x0e, 0x0e, 0x01, 0x01, 0x13, 0x13, 0x01, 0x13,
        0x13, 0x01, 0x13, 0x13, 0x01, 0x13, 0x13, 0x01, 0x0f, 0x13, 0x01,
        0x0d, 0x10, 0x83, 0x0e, 0x10, 0x10, 0x10, 0x13, 0x00,
    ],
    0x4f: [
        0x81, 0x01, 0x0e, 0x10, 0x02, 0x01, 0x02, 0x0f, 0x0c, 0x13, 0x02,
        0x01, 0x02, 0x0e, 0x0c, 0x10, 0x02, 0x01, 0x0d, 0x13, 0x82, 0x0f,
        0x01, 0x06, 0x10, 0x81, 0x18, 0x07, 0x10, 0x82, 0x0e, 0x01, 0x06,
        0x13, 0x81, 0x19, 0x08, 0x13, 0x81, 0x01, 0x00,
    ],
    0x51: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0e, 0x59, 0x02, 0x50, 0x07,
        0x62, 0x81, 0x52, 0x06, 0x59, 0x02, 0x50, 0x07, 0x5b, 0x81, 0x52,
        0x06, 0x59, 0x02, 0x50, 0x07, 0x5a, 0x83, 0x64, 0x56, 0x5b, 0x04,
        0x59, 0x82, 0x5a, 0x50, 0x08, 0x5b, 0x02, 0x5c, 0x81, 0x56, 0x04,
        0x5b, 0x00,
    ],
    0x52: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x04, 0x62, 0x02, 0x63, 0x02,
        0x62, 0x02, 0x63, 0x04, 0x62, 0x02, 0x50, 0x02, 0x59, 0x02, 0x5b,
        0x9b, 0x50, 0x5a, 0x59, 0x59, 0x5a, 0x50, 0x5b, 0x5b, 0x59, 0x59,
        0x50, 0x50, 0x5b, 0x5b, 0x50, 0x5a, 0x5a, 0x59, 0x5b, 0x5b, 0x59,
        0x5a, 0x5a, 0x50, 0x5b, 0x5b, 0x50, 0x04, 0x5a, 0x03, 0x59, 0x02,
        0x5a, 0x03, 0x59, 0x04, 0x5a, 0x10, 0x5b, 0x00,
    ],
    0x53: [
        0x81, 0x50, 0x0f, 0x5a, 0x81, 0x50, 0x0f, 0x5b, 0x81, 0x50, 0x0e,
        0x5a, 0x02, 0x50, 0x02, 0x5b, 0x04, 0x59, 0x02, 0x5b, 0x04, 0x59,
        0x02, 0x5b, 0x81, 0x50, 0x03, 0x5a, 0x04, 0x59, 0x02, 0x5a, 0x04,
        0x59, 0x03, 0x5a, 0x10, 0x5b, 0x00,
    ],
    0x54: [
        0x08, 0x5a, 0x81, 0x53, 0x06, 0x5a, 0x81, 0x50, 0x05, 0x5b, 0x02,
        0x59, 0x84, 0x5b, 0x55, 0x5b, 0x5b, 0x04, 0x59, 0x02, 0x50, 0x04,
        0x5a, 0x02, 0x59, 0x81, 0x54, 0x03, 0x5a, 0x02, 0x59, 0x02, 0x5b,
        0x02, 0x50, 0x04, 0x59, 0x02, 0x5b, 0x83, 0x56, 0x5b, 0x5b, 0x03,
        0x59, 0x02, 0x5a, 0x87, 0x50, 0x5a, 0x59, 0x59, 0x5b, 0x5b, 0x50,
        0x03, 0x5a, 0x83, 0x53, 0x59, 0x5b, 0x03, 0x59, 0x81, 0x50, 0x03,
        0x5b, 0x83, 0x58, 0x5c, 0x5c, 0x03, 0x5b, 0x83, 0x65, 0x63, 0x65,
        0x03, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x55: [
        0x81, 0x50, 0x0f, 0x5a, 0x81, 0x50, 0x0f, 0x59, 0x81, 0x50, 0x0f,
        0x59, 0x81, 0x50, 0x0f, 0x59, 0x83, 0x50, 0x68, 0x69, 0x0d, 0x59,
        0x83, 0x50, 0x6a, 0x6b, 0x0d, 0x5b, 0x00,
    ],
    0x56: [
        0x0f, 0x67, 0x81, 0x6c, 0x0f, 0x67, 0x81, 0x6c, 0x0f, 0x67, 0x81,
        0x6c, 0x0f, 0x67, 0x81, 0x6c, 0x10, 0x67, 0x10, 0x66, 0x00,
    ],
    0x59: [
        0x81, 0x50, 0x04, 0x5a, 0x81, 0x54, 0x0a, 0x5a, 0x81, 0x50, 0x03,
        0x59, 0x8d, 0x5b, 0x56, 0x5b, 0x5b, 0x59, 0x5d, 0x59, 0x5d, 0x59,
        0x5e, 0x5e, 0x5b, 0x50, 0x03, 0x59, 0x03, 0x5a, 0x8a, 0x50, 0x59,
        0x5a, 0x59, 0x5a, 0x59, 0x5a, 0x5a, 0x50, 0x50, 0x03, 0x5b, 0x03,
        0x59, 0x81, 0x50, 0x07, 0x59, 0x81, 0x50, 0x04, 0x5a, 0x03, 0x59,
        0x03, 0x64, 0x81, 0x50, 0x04, 0x62, 0x81, 0x50, 0x0a, 0x5b, 0x81,
        0x50, 0x04, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x5a: [
        0x03, 0x5a, 0x81, 0x53, 0x0b, 0x5a, 0x85, 0x50, 0x5b, 0x59, 0x59,
        0x51, 0x04, 0x5b, 0x05, 0x59, 0x02, 0x5b, 0x02, 0x50, 0x83, 0x5b,
        0x59, 0x51, 0x03, 0x5a, 0x81, 0x50, 0x03, 0x5b, 0x02, 0x59, 0x02,
        0x5a, 0x02, 0x50, 0x87, 0x5a, 0x59, 0x51, 0x62, 0x62, 0x63, 0x65,
        0x03, 0x5c, 0x04, 0x5b, 0x02, 0x50, 0x02, 0x59, 0x83, 0x55, 0x59,
        0x59, 0x0a, 0x5a, 0x85, 0x50, 0x5b, 0x5b, 0x5c, 0x61, 0x0b, 0x5b,
        0x00,
    ],
    0x5b: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x07, 0x59, 0x02, 0x5b, 0x05,
        0x59, 0x02, 0x50, 0x8b, 0x5b, 0x59, 0x59, 0x5b, 0x5b, 0x59, 0x59,
        0x5a, 0x5c, 0x61, 0x5b, 0x03, 0x59, 0x02, 0x50, 0x85, 0x5a, 0x59,
        0x59, 0x53, 0x5a, 0x03, 0x59, 0x02, 0x5a, 0x81, 0x54, 0x03, 0x59,
        0x82, 0x50, 0x5a, 0x03, 0x59, 0x81, 0x51, 0x06, 0x59, 0x81, 0x52,
        0x03, 0x59, 0x81, 0x5a, 0x04, 0x5b, 0x81, 0x55, 0x06, 0x5b, 0x81,
        0x56, 0x04, 0x5b, 0x00,
    ],
    0x5c: [
        0x81, 0x50, 0x06, 0x5a, 0x81, 0x53, 0x07, 0x5a, 0x02, 0x50, 0x05,
        0x59, 0x82, 0x5b, 0x55, 0x03, 0x5b, 0x02, 0x59, 0x02, 0x5b, 0x02,
        0x50, 0x85, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x05, 0x5a, 0x02, 0x59,
        0x02, 0x5a, 0x02, 0x50, 0x84, 0x5a, 0x59, 0x59, 0x5a, 0x06, 0x59,
        0x04, 0x5b, 0x82, 0x50, 0x5a, 0x0a, 0x59, 0x05, 0x5a, 0x10, 0x5b,
        0x00,
    ],
    0x5d: [
        0x81, 0x50, 0x06, 0x5a, 0x81, 0x50, 0x08, 0x5a, 0x81, 0x50, 0x03,
        0x59, 0x03, 0x5b, 0x83, 0x50, 0x5b, 0x5b, 0x05, 0x59, 0x86, 0x5b,
        0x50, 0x59, 0x59, 0x5b, 0x54, 0x04, 0x5a, 0x82, 0x53, 0x5b, 0x04,
        0x59, 0x02, 0x50, 0x02, 0x59, 0x88, 0x5a, 0x56, 0x5b, 0x5b, 0x59,
        0x59, 0x55, 0x5a, 0x04, 0x59, 0x82, 0x50, 0x5a, 0x03, 0x59, 0x02,
        0x5a, 0x84, 0x53, 0x59, 0x59, 0x5a, 0x05, 0x59, 0x81, 0x5a, 0x06,
        0x5b, 0x81, 0x55, 0x09, 0x5b, 0x00,
    ],
    0x5e: [
        0x0f, 0x5a, 0x81, 0x50, 0x03, 0x5b, 0x05, 0x59, 0x07, 0x5b, 0x02,
        0x50, 0x84, 0x5a, 0x50, 0x5d, 0x5d, 0x03, 0x59, 0x07, 0x5a, 0x02,
        0x50, 0x86, 0x59, 0x5a, 0x5a, 0x50, 0x5d, 0x5d, 0x08, 0x59, 0x82,
        0x50, 0x5a, 0x03, 0x59, 0x02, 0x5a, 0x83, 0x50, 0x5d, 0x5d, 0x06,
        0x59, 0x81, 0x50, 0x06, 0x5b, 0x02, 0x5c, 0x81, 0x50, 0x06, 0x5b,
        0x81, 0x50, 0x00,
    ],
    0x61: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0c, 0x5b, 0x02, 0x59, 0x02,
        0x50, 0x0c, 0x5a, 0x02, 0x59, 0x02, 0x50, 0x02, 0x59, 0x0c, 0x5b,
        0x02, 0x50, 0x02, 0x59, 0x0c, 0x5a, 0x02, 0x50, 0x0e, 0x5b, 0x81,
        0x50, 0x00,
    ],
    0x62: [
        0x81, 0x50, 0x08, 0x5a, 0x81, 0x53, 0x05, 0x5a, 0x02, 0x50, 0x05,
        0x5b, 0x03, 0x59, 0x81, 0x51, 0x05, 0x59, 0x02, 0x50, 0x05, 0x5a,
        0x03, 0x59, 0x88, 0x51, 0x59, 0x5b, 0x5b, 0x59, 0x59, 0x50, 0x50,
        0x03, 0x59, 0x05, 0x5b, 0x88, 0x55, 0x59, 0x5a, 0x53, 0x59, 0x59,
        0x50, 0x50, 0x03, 0x59, 0x06, 0x5a, 0x02, 0x59, 0x85, 0x51, 0x59,
        0x59, 0x5a, 0x50, 0x09, 0x5b, 0x02, 0x5d, 0x81, 0x55, 0x03, 0x5b,
        0x00,
    ],
    0x63: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0a, 0x5b, 0x04, 0x59, 0x02,
        0x50, 0x09, 0x5a, 0x81, 0x53, 0x04, 0x59, 0x02, 0x50, 0x03, 0x59,
        0x0b, 0x5b, 0x82, 0x50, 0x5a, 0x03, 0x59, 0x0c, 0x5a, 0x81, 0x5b,
        0x05, 0x5e, 0x0a, 0x5b, 0x00,
    ],
    0x64: [
        0x81, 0x50, 0x0f, 0x5a, 0x8d, 0x50, 0x59, 0x59, 0x5b, 0x5b, 0x59,
        0x59, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x59, 0x03, 0x5b, 0x94, 0x50,
        0x59, 0x59, 0x53, 0x5a, 0x59, 0x59, 0x5a, 0x59, 0x59, 0x54, 0x59,
        0x59, 0x5a, 0x5a, 0x50, 0x50, 0x5b, 0x59, 0x51, 0x06, 0x59, 0x81,
        0x52, 0x04, 0x59, 0x85, 0x50, 0x5a, 0x5a, 0x59, 0x51, 0x06, 0x59,
        0x03, 0x64, 0x02, 0x62, 0x81, 0x50, 0x03, 0x5b, 0x81, 0x55, 0x0b,
        0x5b, 0x81, 0x50, 0x00,
    ],
    0x65: [
        0x10, 0x5a, 0x81, 0x5b, 0x0e, 0x5e, 0x82, 0x5b, 0x50, 0x0e, 0x5a,
        0x02, 0x50, 0x03, 0x5b, 0x08, 0x59, 0x03, 0x5b, 0x02, 0x50, 0x03,
        0x5a, 0x08, 0x59, 0x04, 0x5a, 0x81, 0x50, 0x0f, 0x5b, 0x00,
    ],
    0x66: [
        0x0f, 0x5a, 0x81, 0x50, 0x0f, 0x5b, 0x02, 0x50, 0x04, 0x5a, 0x81,
        0x60, 0x07, 0x5a, 0x02, 0x5c, 0x02, 0x50, 0x02, 0x5b, 0x02, 0x59,
        0x9d, 0x61, 0x59, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x59, 0x60, 0x5a,
        0x50, 0x5a, 0x5a, 0x5c, 0x61, 0x5b, 0x5c, 0x5b, 0x5c, 0x61, 0x59,
        0x60, 0x59, 0x59, 0x61, 0x59, 0x50, 0x5b, 0x5b, 0x07, 0x5c, 0x87,
        0x5b, 0x61, 0x5b, 0x5b, 0x5c, 0x5b, 0x50, 0x00,
    ],
    0x69: [
        0x06, 0x5a, 0x81, 0x54, 0x08, 0x5a, 0x81, 0x50, 0x05, 0x5b, 0x84,
        0x59, 0x56, 0x5b, 0x5b, 0x04, 0x59, 0x02, 0x5b, 0x02, 0x50, 0x04,
        0x5a, 0x84, 0x59, 0x5a, 0x5a, 0x50, 0x04, 0x59, 0x02, 0x5a, 0x02,
        0x50, 0x07, 0x59, 0x83, 0x50, 0x5b, 0x5b, 0x04, 0x59, 0x02, 0x50,
        0x81, 0x64, 0x05, 0x62, 0x84, 0x64, 0x50, 0x5a, 0x5a, 0x04, 0x59,
        0x82, 0x5a, 0x50, 0x07, 0x5b, 0x81, 0x50, 0x07, 0x5b, 0x00,
    ],
    0x6a: [
        0x81, 0x50, 0x0f, 0x5a, 0x81, 0x50, 0x04, 0x59, 0x81, 0x5b, 0x03,
        0x59, 0x81, 0x5b, 0x03, 0x59, 0x03, 0x5b, 0x94, 0x50, 0x59, 0x59,
        0x5b, 0x59, 0x5a, 0x59, 0x5b, 0x59, 0x5a, 0x59, 0x5b, 0x59, 0x5a,
        0x5a, 0x50, 0x50, 0x59, 0x59, 0x5a, 0x03, 0x59, 0x81, 0x5a, 0x03,
        0x59, 0x81, 0x5a, 0x03, 0x59, 0x82, 0x50, 0x5a, 0x0e, 0x59, 0x81,
        0x50, 0x0f, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x6b: [
        0x10, 0x5a, 0x10, 0x5b, 0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x03,
        0x5b, 0x08, 0x59, 0x03, 0x5b, 0x02, 0x50, 0x03, 0x5a, 0x08, 0x59,
        0x03, 0x5a, 0x02, 0x50, 0x0e, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x6c: [
        0x0f, 0x5a, 0x83, 0x50, 0x5b, 0x5b, 0x0d, 0x59, 0x02, 0x50, 0x84,
        0x5a, 0x59, 0x5b, 0x5b, 0x0a, 0x59, 0x02, 0x50, 0x02, 0x59, 0x02,
        0x5a, 0x02, 0x59, 0x02, 0x5b, 0x06, 0x59, 0x02, 0x50, 0x06, 0x59,
        0x02, 0x5a, 0x02, 0x59, 0x02, 0x5b, 0x02, 0x59, 0x82, 0x5a, 0x50,
        0x03, 0x5b, 0x05, 0x5e, 0x02, 0x5b, 0x02, 0x5c, 0x03, 0x5b, 0x00,
    ],
    0x6d: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0b, 0x5b, 0x03, 0x59, 0x02,
        0x50, 0x0a, 0x5a, 0x81, 0x53, 0x03, 0x59, 0x02, 0x50, 0x03, 0x59,
        0x0b, 0x5b, 0x82, 0x50, 0x5a, 0x03, 0x59, 0x0c, 0x5a, 0x81, 0x5b,
        0x07, 0x5e, 0x08, 0x5b, 0x00,
    ],
    0x6e: [
        0x81, 0x50, 0x0f, 0x5a, 0x81, 0x50, 0x03, 0x59, 0x02, 0x5b, 0x08,
        0x59, 0x02, 0x5b, 0x81, 0x50, 0x03, 0x59, 0x02, 0x5a, 0x08, 0x59,
        0x83, 0x5a, 0x50, 0x50, 0x05, 0x5b, 0x09, 0x59, 0x81, 0x50, 0x05,
        0x5a, 0x81, 0x60, 0x09, 0x59, 0x81, 0x50, 0x05, 0x5b, 0x81, 0x61,
        0x09, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x71: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x8b, 0x5b, 0x59, 0x59, 0x5b,
        0x59, 0x59, 0x5b, 0x59, 0x59, 0x5b, 0x5b, 0x03, 0x59, 0x02, 0x50,
        0x8b, 0x5a, 0x59, 0x59, 0x5a, 0x59, 0x59, 0x5a, 0x59, 0x59, 0x5a,
        0x53, 0x03, 0x59, 0x02, 0x50, 0x0a, 0x59, 0x86, 0x51, 0x5b, 0x59,
        0x59, 0x50, 0x5a, 0x0a, 0x59, 0x85, 0x51, 0x5a, 0x59, 0x59, 0x5a,
        0x0b, 0x5b, 0x81, 0x55, 0x04, 0x5b, 0x00,
    ],
    0x72: [
        0x84, 0x50, 0x5a, 0x5a, 0x60, 0x05, 0x5a, 0x81, 0x60, 0x05, 0x5a,
        0x02, 0x50, 0x02, 0x59, 0x81, 0x5f, 0x05, 0x59, 0x81, 0x5f, 0x05,
        0x59, 0x02, 0x50, 0x02, 0x5b, 0x8e, 0x65, 0x5b, 0x59, 0x59, 0x5b,
        0x59, 0x61, 0x59, 0x59, 0x5b, 0x59, 0x5b, 0x50, 0x50, 0x03, 0x5a,
        0x8d, 0x60, 0x59, 0x59, 0x60, 0x59, 0x5a, 0x59, 0x59, 0x60, 0x59,
        0x5a, 0x50, 0x5a, 0x03, 0x59, 0x8c, 0x61, 0x59, 0x59, 0x5f, 0x5b,
        0x59, 0x59, 0x5b, 0x61, 0x59, 0x59, 0x5a, 0x04, 0x5b, 0x8c, 0x5c,
        0x5b, 0x5b, 0x61, 0x5c, 0x5b, 0x5b, 0x5c, 0x5c, 0x61, 0x5b, 0x5b,
        0x00,
    ],
    0x73: [
        0x81, 0x50, 0x09, 0x5a, 0x02, 0x5c, 0x03, 0x5a, 0x02, 0x50, 0x02,
        0x5b, 0x03, 0x59, 0x02, 0x5b, 0x02, 0x59, 0x02, 0x5a, 0x03, 0x59,
        0x02, 0x50, 0x02, 0x5a, 0x02, 0x5b, 0x87, 0x59, 0x5a, 0x5a, 0x59,
        0x59, 0x5e, 0x5e, 0x03, 0x59, 0x02, 0x50, 0x8b, 0x5b, 0x59, 0x5a,
        0x5a, 0x59, 0x5d, 0x5d, 0x59, 0x59, 0x5a, 0x5a, 0x03, 0x59, 0x83,
        0x50, 0x5a, 0x5a, 0x04, 0x59, 0x02, 0x5a, 0x07, 0x59, 0x81, 0x5a,
        0x10, 0x5b, 0x00,
    ],
    0x74: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0a, 0x5b, 0x04, 0x59, 0x02,
        0x50, 0x09, 0x5a, 0x81, 0x53, 0x04, 0x59, 0x02, 0x50, 0x03, 0x59,
        0x0b, 0x5b, 0x82, 0x50, 0x5a, 0x03, 0x59, 0x0b, 0x5a, 0x81, 0x50,
        0x0f, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x75: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0c, 0x59, 0x02, 0x5b, 0x02,
        0x50, 0xa0, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x59,
        0x5b, 0x59, 0x59, 0x5a, 0x5a, 0x50, 0x50, 0x5a, 0x59, 0x59, 0x5a,
        0x59, 0x59, 0x60, 0x59, 0x59, 0x60, 0x59, 0x59, 0x5b, 0x5b, 0x50,
        0x50, 0x06, 0x59, 0x8a, 0x5f, 0x59, 0x59, 0x5f, 0x59, 0x59, 0x60,
        0x5a, 0x50, 0x50, 0x06, 0x5b, 0x89, 0x61, 0x5b, 0x5b, 0x61, 0x5b,
        0x5b, 0x61, 0x5b, 0x50, 0x00,
    ],
    0x76: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x0a, 0x5b, 0x02, 0x59, 0x02,
        0x5b, 0x02, 0x50, 0x0a, 0x5a, 0x02, 0x59, 0x02, 0x5a, 0x02, 0x50,
        0x0e, 0x5b, 0x02, 0x50, 0x0f, 0x5a, 0x81, 0x50, 0x0f, 0x5b, 0x00,
    ],
    0x7a: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x02, 0x59, 0x02, 0x5b, 0x02,
        0x59, 0xa0, 0x5b, 0x59, 0x59, 0x5b, 0x59, 0x5b, 0x59, 0x59, 0x50,
        0x50, 0x59, 0x59, 0x5a, 0x50, 0x59, 0x59, 0x50, 0x59, 0x59, 0x50,
        0x59, 0x54, 0x59, 0x59, 0x50, 0x50, 0x5b, 0x59, 0x59, 0x50, 0x5b,
        0x5b, 0x04, 0x65, 0x8a, 0x5b, 0x56, 0x5b, 0x5b, 0x50, 0x5a, 0x5a,
        0x59, 0x59, 0x50, 0x0b, 0x5a, 0x04, 0x5b, 0x81, 0x50, 0x0b, 0x5b,
        0x00,
    ],
    0x7b: [
        0x81, 0x50, 0x03, 0x5a, 0x81, 0x54, 0x0a, 0x5a, 0x02, 0x50, 0x02,
        0x59, 0x82, 0x5b, 0x56, 0x06, 0x5b, 0x02, 0x59, 0x02, 0x5b, 0x02,
        0x50, 0x02, 0x59, 0x82, 0x5a, 0x54, 0x05, 0x5a, 0x8d, 0x53, 0x59,
        0x59, 0x5a, 0x5a, 0x50, 0x50, 0x5b, 0x59, 0x59, 0x52, 0x59, 0x59,
        0x03, 0x5b, 0x8d, 0x55, 0x5b, 0x5b, 0x59, 0x59, 0x50, 0x5a, 0x5a,
        0x59, 0x59, 0x52, 0x59, 0x59, 0x06, 0x5a, 0x02, 0x59, 0x81, 0x5a,
        0x04, 0x5b, 0x81, 0x56, 0x0b, 0x5b, 0x00,
    ],
    0x7c: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x81, 0x5b, 0x04, 0x5e, 0x03,
        0x5d, 0x02, 0x5b, 0x02, 0x59, 0x02, 0x5b, 0x02, 0x50, 0x0a, 0x5a,
        0x02, 0x59, 0x02, 0x5a, 0x02, 0x50, 0x02, 0x5b, 0x02, 0x59, 0x04,
        0x5d, 0x06, 0x5b, 0x86, 0x50, 0x5a, 0x5a, 0x50, 0x5b, 0x59, 0x0a,
        0x5a, 0x85, 0x50, 0x5b, 0x5b, 0x5c, 0x5c, 0x03, 0x5b, 0x02, 0x5d,
        0x81, 0x5b, 0x03, 0x5e, 0x02, 0x5b, 0x81, 0x50, 0x00,
    ],
    0x7d: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x02, 0x5b, 0x0c, 0x59, 0x02,
        0x50, 0x02, 0x5c, 0x02, 0x5b, 0x83, 0x59, 0x5b, 0x52, 0x07, 0x59,
        0x02, 0x50, 0x03, 0x5a, 0x84, 0x50, 0x59, 0x5a, 0x56, 0x07, 0x5b,
        0x02, 0x50, 0x03, 0x59, 0x83, 0x50, 0x59, 0x59, 0x09, 0x5a, 0x81,
        0x50, 0x03, 0x5b, 0x81, 0x5c, 0x0b, 0x5b, 0x00,
    ],
    0x7e: [
        0x81, 0x50, 0x0e, 0x5a, 0x02, 0x50, 0x04, 0x5b, 0x03, 0x59, 0x07,
        0x5b, 0x02, 0x50, 0x02, 0x5a, 0x85, 0x50, 0x5c, 0x5b, 0x59, 0x59,
        0x07, 0x5a, 0x02, 0x50, 0x87, 0x5b, 0x59, 0x5a, 0x5a, 0x50, 0x5b,
        0x5b, 0x07, 0x59, 0x89, 0x50, 0x5a, 0x50, 0x5b, 0x5b, 0x59, 0x5a,
        0x5a, 0x50, 0x03, 0x5b, 0x04, 0x59, 0x82, 0x5a, 0x5b, 0x03, 0x5c,
        0x03, 0x5b, 0x03, 0x5c, 0x81, 0x50, 0x05, 0x5b, 0x00,
    ],
    0x82: [
        0x85, 0x50, 0x5c, 0x5a, 0x5a, 0x54, 0x0a, 0x5a, 0x02, 0x50, 0x84,
        0x5a, 0x59, 0x5b, 0x56, 0x05, 0x5b, 0x03, 0x59, 0x02, 0x5b, 0x02,
        0x50, 0x02, 0x59, 0x82, 0x5a, 0x54, 0x04, 0x5a, 0x81, 0x53, 0x03,
        0x59, 0x02, 0x5a, 0x02, 0x50, 0x84, 0x5b, 0x59, 0x59, 0x52, 0x04,
        0x59, 0x81, 0x51, 0x05, 0x59, 0x88, 0x50, 0x5a, 0x5a, 0x59, 0x59,
        0x52, 0x59, 0x59, 0x05, 0x64, 0x03, 0x59, 0x81, 0x5a, 0x04, 0x5b,
        0x81, 0x56, 0x0b, 0x5b, 0x00,
    ],
}


def generate_mods(o: bytes) -> None:
    map_indexes: List[int] = []
    rooms: Dict[int, List[int]] = {}
    size = 0

    for row in range(17):
        for col in range(8):
            index_address = rom_info.terrain_index_13725 + row * 65 + 1 + col * 8
            data_lo = o[index_address]
            # verified[index_address] = data_lo
            data_hi = o[index_address + 1]
            # verified[index_address + 1] = data_hi
            map_index = o[index_address + 3]
            # verified[index_address + 3] = map_index
            # for now at least, this is the 1st assertion that someone with the wrong rom version runs into
            error = "terrain index matching map index - Is this the correct version of the rom?"
            assert map_index == row * 8 + col, error
            address = ((data_hi << 8) | data_lo) + TerrainCompressor.BANK_OFFSET

            assert (map_index != 0x0a) or (address == rom_info.terrain_begin_10ef0), f"first room address {address}"

            if address < rom_info.terrain_begin_10ef0 or address >= rom_info.terrain_end_120da:
                continue  # hallways

            cursor = address
            original_compressed_bytes: List[int] = []
            while o[cursor] != 0:
                original_compressed_bytes.append(o[cursor])
                # verified[cursor] = rom[cursor]
                cursor += 1
            original_compressed_bytes.append(0x00)  # just for consistency
            # verified[cursor] = 0x00

            decompressed = TerrainCompressor.decompress(original_compressed_bytes)
            if map_index == 0x0b:
                # This room has 2 extra bytes past the end of the room.
                # I'm guessing it's a typo in the rom.
                #
                # (Someone ended the room with 02 3b. That was a visible bug,
                #  so some else said "It needs to end with 03 3b."
                #  So someone tacked on a 03 3b after the 02 3b,
                #  instead of replacing it.)
                #
                # And I'm guessing it doesn't have any effect on the game. 🤞
                # (I don't know the effect of writing 2 bytes past the end of the room.)
                decompressed = decompressed[:-2]
            assert len(decompressed) == 96
            recompressed = TerrainCompressor.compress(decompressed)

            # update class data
            map_indexes.append(map_index)
            rooms[map_index] = recompressed
            size += len(recompressed)
            # print(len(recompressed))

    original_size = rom_info.terrain_end_120da - rom_info.terrain_begin_10ef0
    assert original_size - size == 77, f"original terrain size: {original_size}  recompressed: {size}"
    # print(f"average compressed size: {self._size / len(self._map_indexes)}")
    # print(f"average original size: {original_size / len(self._map_indexes)}")
    # print(f"room count: {len(self._map_indexes)}")

    """
    with open("verified_.py", "wt") as file:
        file.write("verified = {\n")
        for key in verified:
            file.write(f"    {hex(key)}: {hex(verified[key])},\n")
        print("}\n")
    """

    assert all(map_index in map_indexes for map_index in rooms)
    assert all(map_index in rooms for map_index in map_indexes)

    def hex_list(bs: List[int]) -> str:
        tr = "[\n        "
        len_since_newline = 8
        for b in bs:
            if len_since_newline >= 73:
                tr = tr[:-1] + "\n        "
                len_since_newline = 8
            assert b < 256, bs
            tr += f"0x{b:02x}, "
            len_since_newline += 6
        tr = tr[:-1] + "\n    ],"
        return tr

    for map_index, room in rooms.items():
        print(f"    0x{map_index:02x}: {hex_list(room)}")
