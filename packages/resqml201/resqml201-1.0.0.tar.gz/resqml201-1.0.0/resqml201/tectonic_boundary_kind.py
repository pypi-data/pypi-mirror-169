from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class TectonicBoundaryKind(Enum):
    """
    Enumeration of the types of tectonic boundaries.

    :cvar FAULT: Fracture with displacement
    :cvar FRACTURE: Fracture
    """
    FAULT = "fault"
    FRACTURE = "fracture"
