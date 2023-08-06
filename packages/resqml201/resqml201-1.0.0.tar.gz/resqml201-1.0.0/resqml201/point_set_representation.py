from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_point_set_representation import ObjPointSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointSetRepresentation(ObjPointSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
