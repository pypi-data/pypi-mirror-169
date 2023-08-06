from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactSide(Enum):
    """Enumeration that specifies the location of the contacts, chosen from the
    attributes listed below.

    For example, if you specify contact between a horizon and a fault,
    you can specify if the contact is on the foot wall side or the
    hanging wall side of the fault, and if the fault is splitting both
    sides of a horizon or the older side only. From Wikipedia:
    http://en.wikipedia.org/wiki/Foot_wall CC-BY-SA-3.0-MIGRATED; GFDL-
    WITH-DISCLAIMERS Released under the GNU Free Documentation License.

    :cvar FOOTWALL: The footwall side of the fault. See picture.
    :cvar HANGING_WALL: The hanging wall side of the fault. See picture.
    :cvar NORTH: For a vertical fault, specification of the north side.
    :cvar SOUTH: For a vertical fault, specification of the south side.
    :cvar EAST: For a vertical fault, specification of the east side.
    :cvar WEST: For a vertical fault, specification of the west side.
    :cvar YOUNGER: Indicates that a fault splits a genetic boundary on
        its younger side.
    :cvar OLDER: Indicates that a fault splits a genetic boundary on its
        older side.
    :cvar BOTH: Indicates that a fault splits both sides of a genetic
        feature.
    """
    FOOTWALL = "footwall"
    HANGING_WALL = "hanging wall"
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    YOUNGER = "younger"
    OLDER = "older"
    BOTH = "both"
