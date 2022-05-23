from dataclasses import dataclass

""" codes - first byte of item data structure in rom """
KEYWORD = 0x0A
RESCUE = 0x2A
NORMAL = 0x26
MAIN = 0x0D


@dataclass
class Item:
    name: str
    """ for display """
    debug_name: str
    """ human readable unique identifier """
    is_progression: bool
    """ this item can open up new areas in the game """
    required: bool
    """ this item can be required to win (never_exclude in AP api) """
    multiworld: bool
    """ this item should be randomized to other worlds in a multiworld """
    code: int
    """ first byte in rom item data structure (not unique) """
    # Archipelago uses `code` property, so I might want to rename this
    id: int
    """ sixth byte in rom item data structure (not unique) """


items = [
    Item("Key Word", "keyword_0", True, False, False, KEYWORD, 0x00),
    Item("Key Word", "keyword_1", True, False, False, KEYWORD, 0x01),
    Item("Key Word", "keyword_2", True, False, False, KEYWORD, 0x02),
    Item("Key Word", "keyword_3", True, False, False, KEYWORD, 0x03),
    Item("Empty", "empty", False, False, True, NORMAL, 0x04),
    Item("ID Card", "card", False, False, True, NORMAL, 0x05),
    # TODO: skip in progression balancing - doesn't do any good to push these forward
    Item("Red ID Card", "red", False, True, True, NORMAL, 0x06),
    Item("Floppy Disk", "floppy", False, True, True, NORMAL, 0x07),

    Item("Bread", "bread", False, False, False, NORMAL, 0x08),
    Item("Opa-Opa", "opa", True, True, True, NORMAL, 0x09),
    Item("Zillion", "gun", True, True, True, NORMAL, 0x0A),
    Item("Scope", "scope", False, False, True, NORMAL, 0x0B),
    # custom items here

    # rescue
    Item("Apple", "rescue_0", True, True, True, RESCUE, 0x00),
    Item("Champ", "rescue_1", True, True, True, RESCUE, 0x01),
]

MAIN_ITEM = Item("Main Computer", "main", False, True, False, MAIN, 0x00)
