from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.boundary_relation import BoundaryRelation
from resqml201.obj_boundary_feature_interpretation import ObjBoundaryFeatureInterpretation
from resqml201.sequence_stratigraphy_surface import SequenceStratigraphySurface

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjHorizonInterpretation(ObjBoundaryFeatureInterpretation):
    """A type of boundary feature, the class specifies if the boundary feature
    is a horizon. Maximum Flooding Surface.

    - Transgressive Surface ( for erosion or intrusion ?)
    - Sequence Boundary
    - Stratigraphic Limit
    """
    class Meta:
        name = "obj_HorizonInterpretation"

    boundary_relation: List[BoundaryRelation] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    sequence_stratigraphy_surface: Optional[SequenceStratigraphySurface] = field(
        default=None,
        metadata={
            "name": "SequenceStratigraphySurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
