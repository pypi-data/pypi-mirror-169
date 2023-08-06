from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_geobody_boundary_interpretation import ObjGeobodyBoundaryInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeobodyBoundaryInterpretation(ObjGeobodyBoundaryInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
