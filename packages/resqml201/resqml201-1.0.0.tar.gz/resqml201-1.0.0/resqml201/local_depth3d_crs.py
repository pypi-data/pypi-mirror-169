from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_local_depth3d_crs import ObjLocalDepth3DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalDepth3DCrs(ObjLocalDepth3DCrs):
    class Meta:
        name = "LocalDepth3dCrs"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
