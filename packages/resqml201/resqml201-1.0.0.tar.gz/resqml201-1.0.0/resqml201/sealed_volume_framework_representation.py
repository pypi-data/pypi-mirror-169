from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_sealed_volume_framework_representation import ObjSealedVolumeFrameworkRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedVolumeFrameworkRepresentation(ObjSealedVolumeFrameworkRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
