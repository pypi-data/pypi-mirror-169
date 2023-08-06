from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyLengthPerAreaUom(Enum):
    """
    :cvar J_M_M2: joule metre per square metre
    :cvar KCAL_TH_M_CM2: thousand calorie metre per square centimetre
    """
    J_M_M2 = "J.m/m2"
    KCAL_TH_M_CM2 = "kcal[th].m/cm2"
