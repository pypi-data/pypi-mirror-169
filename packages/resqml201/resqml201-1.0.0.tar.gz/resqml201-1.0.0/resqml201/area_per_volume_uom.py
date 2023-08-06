from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AreaPerVolumeUom(Enum):
    """
    :cvar VALUE_1_M: per metre
    :cvar B_CM3: barn per cubic centimetre
    :cvar CU: capture unit
    :cvar FT2_IN3: square foot per cubic inch
    :cvar M2_CM3: square metre per cubic centimetre
    :cvar M2_M3: square metre per cubic metre
    """
    VALUE_1_M = "1/m"
    B_CM3 = "b/cm3"
    CU = "cu"
    FT2_IN3 = "ft2/in3"
    M2_CM3 = "m2/cm3"
    M2_M3 = "m2/m3"
