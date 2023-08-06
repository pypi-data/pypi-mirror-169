from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalLengthUom(Enum):
    """
    :cvar VALUE_1_ANGSTROM: per angstrom
    :cvar VALUE_1_CM: per centimetre
    :cvar VALUE_1_FT: per foot
    :cvar VALUE_1_IN: per inch
    :cvar VALUE_1_M: per metre
    :cvar VALUE_1_MI: per mile
    :cvar VALUE_1_MM: per millimetre
    :cvar VALUE_1_NM: per nanometre
    :cvar VALUE_1_YD: per yard
    :cvar VALUE_1_E_9_1_FT: per thousand million foot
    """
    VALUE_1_ANGSTROM = "1/angstrom"
    VALUE_1_CM = "1/cm"
    VALUE_1_FT = "1/ft"
    VALUE_1_IN = "1/in"
    VALUE_1_M = "1/m"
    VALUE_1_MI = "1/mi"
    VALUE_1_MM = "1/mm"
    VALUE_1_NM = "1/nm"
    VALUE_1_YD = "1/yd"
    VALUE_1_E_9_1_FT = "1E-9 1/ft"
