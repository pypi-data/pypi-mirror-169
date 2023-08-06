from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.fluid_contact import FluidContact
from resqml201.obj_boundary_feature import ObjBoundaryFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjFluidBoundaryFeature(ObjBoundaryFeature):
    """A boundary (usually a plane) separating two fluid phases, such as a gas-
    oil contact (GOC), a water-oil contact (WOC), a gas-oil contact (GOC), or
    others.

    For types, see FluidContact.
    """
    class Meta:
        name = "obj_FluidBoundaryFeature"

    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
