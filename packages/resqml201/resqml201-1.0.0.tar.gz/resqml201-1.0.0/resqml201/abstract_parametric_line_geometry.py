from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_geometry import AbstractGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractParametricLineGeometry(AbstractGeometry):
    """
    The abstract class for defining a single parametric line.
    """
