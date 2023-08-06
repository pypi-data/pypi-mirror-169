from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_polyline_representation import ObjPolylineRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PolylineRepresentation(ObjPolylineRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
