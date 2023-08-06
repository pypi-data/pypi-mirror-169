from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.obj_geologic_unit_interpretation import ObjGeologicUnitInterpretation
from resqml201.phase import Phase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjRockFluidUnitInterpretation(ObjGeologicUnitInterpretation):
    """
    A type of rock fluid feature interpretation , this class identifies if a
    rock fluid feature by its phase.
    """
    class Meta:
        name = "obj_RockFluidUnitInterpretation"

    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
