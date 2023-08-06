from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyPerMassPerTimeUom(Enum):
    """
    :cvar MREM_H: thousandth of irem per hour
    :cvar M_SV_H: millisievert per hour
    :cvar REM_H: rem per hour
    :cvar SV_H: sievert per hour
    :cvar SV_S: sievert per second
    """
    MREM_H = "mrem/h"
    M_SV_H = "mSv/h"
    REM_H = "rem/h"
    SV_H = "Sv/h"
    SV_S = "Sv/s"
