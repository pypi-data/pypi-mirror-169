from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LengthPerLengthUom(Enum):
    """
    :cvar VALUE: percent
    :cvar VALUE_0_01_FT_FT: foot per hundred foot
    :cvar VALUE_1_30_M_M: metre per thirty metre
    :cvar EUC: euclid
    :cvar FT_FT: foot per foot
    :cvar FT_IN: foot per inch
    :cvar FT_M: foot per metre
    :cvar FT_MI: foot per mile
    :cvar KM_CM: kilometre per centimetre
    :cvar M_CM: metre per centimetre
    :cvar M_KM: metre per kilometre
    :cvar M_M: metre per metre
    :cvar MI_IN: mile per inch
    """
    VALUE = "%"
    VALUE_0_01_FT_FT = "0.01 ft/ft"
    VALUE_1_30_M_M = "1/30 m/m"
    EUC = "Euc"
    FT_FT = "ft/ft"
    FT_IN = "ft/in"
    FT_M = "ft/m"
    FT_MI = "ft/mi"
    KM_CM = "km/cm"
    M_CM = "m/cm"
    M_KM = "m/km"
    M_M = "m/m"
    MI_IN = "mi/in"
