from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.data_object_reference import DataObjectReference
from resqml201.obj_representation_set_representation import ObjRepresentationSetRepresentation
from resqml201.volume_region import VolumeRegion
from resqml201.volume_shell import VolumeShell

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjSealedVolumeFrameworkRepresentation(ObjRepresentationSetRepresentation):
    """A strict boundary representation (BREP), which represents the volume
    region by assembling together shells.

    BUSINESS RULE: The sealed structural framework must be part of the
    same earth model as this sealed volume framework.
    """
    class Meta:
        name = "obj_SealedVolumeFrameworkRepresentation"

    based_on: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    shells: List[VolumeShell] = field(
        default_factory=list,
        metadata={
            "name": "Shells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
    regions: List[VolumeRegion] = field(
        default_factory=list,
        metadata={
            "name": "Regions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
