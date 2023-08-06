from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class GeologicUnitMaterialImplacement(Enum):
    """
    The enumerated attributes of a horizon.
    """
    AUTOCHTONOUS = "autochtonous"
    ALLOCHTONOUS = "allochtonous"
