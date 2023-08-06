from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_rock_fluid_unit_feature import ObjRockFluidUnitFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidUnitFeature(ObjRockFluidUnitFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
