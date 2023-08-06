from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_triangulated_set_representation import ObjTriangulatedSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TriangulatedSetRepresentation(ObjTriangulatedSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
