from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_polyline_set_representation import ObjPolylineSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PolylineSetRepresentation(ObjPolylineSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
