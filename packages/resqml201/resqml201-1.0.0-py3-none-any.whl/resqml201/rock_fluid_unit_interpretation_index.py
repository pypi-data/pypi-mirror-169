from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidUnitInterpretationIndex:
    """
    An element that allows ordering of fluid feature interpretations in a fluid
    organization interpretation.

    :ivar index: Index of the fluid feature interpretation.
    :ivar rock_fluid_unit:
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    rock_fluid_unit: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RockFluidUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
