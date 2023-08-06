from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AmountOfSubstanceUom(Enum):
    """
    :cvar KMOL: kilogram-mole
    :cvar LBMOL: pound-mass-mole
    :cvar MMOL: milligram-mole
    :cvar MOL: gram-mole
    :cvar UMOL: microgram-mole
    """
    KMOL = "kmol"
    LBMOL = "lbmol"
    MMOL = "mmol"
    MOL = "mol"
    UMOL = "umol"
