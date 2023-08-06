from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_points_property import ObjPointsProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointsProperty(ObjPointsProperty):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
