from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class NormalizedPowerUom(Enum):
    """
    :cvar B_W: bel watt
    :cvar D_B_MW: decibel megawatt
    :cvar D_B_M_W_1: decibel milliwatt
    :cvar D_B_W: decibel watt
    """
    B_W = "B.W"
    D_B_MW = "dB.MW"
    D_B_M_W_1 = "dB.mW"
    D_B_W = "dB.W"
