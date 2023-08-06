from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_geologic_feature import AbstractGeologicFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjBoundaryFeature(AbstractGeologicFeature):
    """An interface between two geological objects, such as horizons and
    faults.

    It is a surface object.
    """
    class Meta:
        name = "obj_BoundaryFeature"
