from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_boundary_feature_interpretation import ObjBoundaryFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BoundaryFeatureInterpretation(ObjBoundaryFeatureInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
