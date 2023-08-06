from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_property import AbstractProperty
from resqml201.patch_of_points import PatchOfPoints

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjPointsProperty(AbstractProperty):
    """
    Represents the geometric information that should *not* be used as
    representation geometry, but should be used in another context where the
    location or geometrical vectorial distances are needed.
    """
    class Meta:
        name = "obj_PointsProperty"

    patch_of_points: List[PatchOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "PatchOfPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
