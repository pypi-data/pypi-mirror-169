from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_redefined_geometry_representation import ObjRedefinedGeometryRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RedefinedGeometryRepresentation(ObjRedefinedGeometryRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
