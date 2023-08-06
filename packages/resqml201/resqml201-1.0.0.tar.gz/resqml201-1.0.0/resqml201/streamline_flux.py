from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class StreamlineFlux(Enum):
    """
    Enumeration of the usual streamline fluxes.

    :cvar OIL: Oil Phase flux
    :cvar GAS: Gas Phase flux
    :cvar WATER: Water Phase flux
    :cvar TOTAL: Sum of (Water + Oil + Gas) Phase fluxes
    :cvar OTHER: Used to indicate that another flux is being traced.
        BUSINESS RULE: OtherFlux should appear if this value is
        specified.
    """
    OIL = "oil"
    GAS = "gas"
    WATER = "water"
    TOTAL = "total"
    OTHER = "other"
