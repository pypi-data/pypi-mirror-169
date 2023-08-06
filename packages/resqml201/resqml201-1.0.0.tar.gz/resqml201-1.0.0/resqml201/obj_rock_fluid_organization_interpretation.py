from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml201.rock_fluid_unit_interpretation_index import RockFluidUnitInterpretationIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjRockFluidOrganizationInterpretation(AbstractOrganizationInterpretation):
    """
    Interpretation of the fluid organization units.
    """
    class Meta:
        name = "obj_RockFluidOrganizationInterpretation"

    rock_fluid_unit_index: Optional[RockFluidUnitInterpretationIndex] = field(
        default=None,
        metadata={
            "name": "RockFluidUnitIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
