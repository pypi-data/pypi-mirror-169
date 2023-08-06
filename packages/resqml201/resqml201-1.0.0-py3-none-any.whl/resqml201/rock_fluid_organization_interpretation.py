from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_rock_fluid_organization_interpretation import ObjRockFluidOrganizationInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidOrganizationInterpretation(ObjRockFluidOrganizationInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
