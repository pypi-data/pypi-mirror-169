from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.data_object_reference import DataObjectReference
from resqml201.volume_shell import VolumeShell

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VolumeRegion:
    """
    The volume within a shell or envelope.
    """
    patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    internal_shells: List[VolumeShell] = field(
        default_factory=list,
        metadata={
            "name": "InternalShells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    represents: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Represents",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    external_shell: Optional[VolumeShell] = field(
        default=None,
        metadata={
            "name": "ExternalShell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
