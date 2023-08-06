from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_plane_set_representation import ObjPlaneSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PlaneSetRepresentation(ObjPlaneSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
