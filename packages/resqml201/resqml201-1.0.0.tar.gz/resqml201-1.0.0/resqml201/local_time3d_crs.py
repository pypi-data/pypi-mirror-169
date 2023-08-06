from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_local_time3d_crs import ObjLocalTime3DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalTime3DCrs(ObjLocalTime3DCrs):
    class Meta:
        name = "LocalTime3dCrs"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
