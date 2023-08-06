from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_fluid_boundary_feature import ObjFluidBoundaryFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FluidBoundaryFeature(ObjFluidBoundaryFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
