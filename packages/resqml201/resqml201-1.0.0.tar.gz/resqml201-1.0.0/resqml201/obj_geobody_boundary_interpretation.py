from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.boundary_relation import BoundaryRelation
from resqml201.obj_boundary_feature_interpretation import ObjBoundaryFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeobodyBoundaryInterpretation(ObjBoundaryFeatureInterpretation):
    """
    A type of boundary feature, this class identifies if the boundary is a
    geobody and the type of the boundary.
    """
    class Meta:
        name = "obj_GeobodyBoundaryInterpretation"

    boundary_relation: List[BoundaryRelation] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
