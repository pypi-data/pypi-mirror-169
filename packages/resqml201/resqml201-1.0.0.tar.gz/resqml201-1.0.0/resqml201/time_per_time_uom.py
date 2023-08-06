from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TimePerTimeUom(Enum):
    """
    :cvar VALUE: percent
    :cvar EUC: euclid
    :cvar MS_S: millisecond per second
    :cvar S_S: second per second
    """
    VALUE = "%"
    EUC = "Euc"
    MS_S = "ms/s"
    S_S = "s/s"
