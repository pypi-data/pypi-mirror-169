from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ThrowKind(Enum):
    """
    Enumerations that characterize the throw of the fault interpretation.
    """
    REVERSE = "reverse"
    NORMAL = "normal"
    THRUST = "thrust"
    STRIKE_AND_SLIP = "strike and slip"
    SCISSOR = "scissor"
    VARIABLE = "variable"
