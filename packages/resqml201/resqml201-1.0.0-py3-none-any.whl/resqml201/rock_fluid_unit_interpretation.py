from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_rock_fluid_unit_interpretation import ObjRockFluidUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidUnitInterpretation(ObjRockFluidUnitInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
