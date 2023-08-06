from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalPressureUom(Enum):
    """
    :cvar VALUE_1_BAR: per bar
    :cvar VALUE_1_K_PA: per kilopascal
    :cvar VALUE_1_PA: per pascal
    :cvar VALUE_1_P_PA: per picopascal
    :cvar VALUE_1_PSI: per psi
    :cvar VALUE_1_UPSI: per millionth of psi
    """
    VALUE_1_BAR = "1/bar"
    VALUE_1_K_PA = "1/kPa"
    VALUE_1_PA = "1/Pa"
    VALUE_1_P_PA = "1/pPa"
    VALUE_1_PSI = "1/psi"
    VALUE_1_UPSI = "1/upsi"
