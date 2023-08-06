from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class SequenceStratigraphySurface(Enum):
    """
    The enumerated attributes of a horizon.
    """
    FLOODING = "flooding"
    RAVINEMENT = "ravinement"
    MAXIMUM_FLOODING = "maximum flooding"
    TRANSGRESSIVE = "transgressive"
