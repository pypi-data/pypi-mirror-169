from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_local_grid_set import ObjLocalGridSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalGridSet(ObjLocalGridSet):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
