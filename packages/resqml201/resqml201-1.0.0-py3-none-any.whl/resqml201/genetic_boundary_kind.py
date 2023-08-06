from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class GeneticBoundaryKind(Enum):
    """Enumerations used to indicate a specific type of genetic boundary
    feature.

    See attributes below. Note that a genetic boundary has a younger
    side and an older side.

    :cvar GEOBODY_BOUNDARY: An interface between a geobody and other
        geologic objects.
    :cvar HORIZON: An interface associated with a stratigraphic unit,
        which could be the top or bottom of the unit.
    """
    GEOBODY_BOUNDARY = "geobody boundary"
    HORIZON = "horizon"
