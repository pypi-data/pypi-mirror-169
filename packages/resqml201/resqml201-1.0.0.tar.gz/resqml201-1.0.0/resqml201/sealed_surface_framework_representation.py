from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_sealed_surface_framework_representation import ObjSealedSurfaceFrameworkRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedSurfaceFrameworkRepresentation(ObjSealedSurfaceFrameworkRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
