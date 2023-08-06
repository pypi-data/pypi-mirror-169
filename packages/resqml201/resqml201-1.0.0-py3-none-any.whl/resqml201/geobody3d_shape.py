from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Geobody3DShape(Enum):
    """
    The enumerated attributes of a horizon.
    """
    DYKE = "dyke"
    SILT = "silt"
    DOME = "dome"
    SHEETH = "sheeth"
    DIAPIR = "diapir"
    BATHOLITH = "batholith"
    CHANNEL = "channel"
    DELTA = "delta"
    DUNE = "dune"
    FAN = "fan"
    REEF = "reef"
    WEDGE = "wedge"
