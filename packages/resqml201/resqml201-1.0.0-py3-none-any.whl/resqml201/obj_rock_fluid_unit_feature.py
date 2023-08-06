from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference
from resqml201.obj_geologic_unit_feature import ObjGeologicUnitFeature
from resqml201.phase import Phase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjRockFluidUnitFeature(ObjGeologicUnitFeature):
    """A fluid phase plus one or more stratigraphic units.

    A unit may correspond to a pair of horizons that are not adjacent
    stratigraphically, e.g., a coarse zonation, and is often used to
    define the reservoir. For types, see Phase.
    """
    class Meta:
        name = "obj_RockFluidUnitFeature"

    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    fluid_boundary_bottom: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidBoundaryBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    fluid_boundary_top: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidBoundaryTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
