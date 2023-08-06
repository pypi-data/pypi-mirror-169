from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_non_sealed_surface_framework_representation import ObjNonSealedSurfaceFrameworkRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NonSealedSurfaceFrameworkRepresentation(ObjNonSealedSurfaceFrameworkRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
