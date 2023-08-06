from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Domain(Enum):
    """
    Enumeration for the feature interpretation to specify if the measurement is
    in the seismic time or depth domain or if it is derived from a laboratory
    measurement.

    :cvar DEPTH: Position defined by measurements in the depth domain.
    :cvar TIME: Position based on geophysical measurements in two-way
        time (TWT).
    :cvar MIXED:
    """
    DEPTH = "depth"
    TIME = "time"
    MIXED = "mixed"
