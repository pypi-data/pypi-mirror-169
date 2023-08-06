from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class BoundaryRelation(Enum):
    """
    The enumerated attributes of a horizon.

    :cvar CONFORMABLE: If used uniquely, then it means the horizon is
        conformable above and below. If used with unconformity, then it
        means partial unconformity.
    :cvar UNCONFORMABLE_BELOW_AND_ABOVE:
    :cvar UNCONFORMABLE_ABOVE: If used with conformable, then it means
        partial unconformity.
    :cvar UNCONFORMABLE_BELOW: If used with conformable, then it means
        partial unconformity.
    """
    CONFORMABLE = "conformable"
    UNCONFORMABLE_BELOW_AND_ABOVE = "unconformable below and above"
    UNCONFORMABLE_ABOVE = "unconformable above"
    UNCONFORMABLE_BELOW = "unconformable below"
