from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_point3d_array import AbstractPoint3DArray
from resqml201.grid_geometry_attachment import GridGeometryAttachment

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AdditionalGridPoints:
    """
    Geometry given by means of points attached to additional elements of a
    grid.

    :ivar representation_patch_index: Used to remove ambiguity in
        geometry attachment, if the attachment element is not
        sufficient. Usually required for subnodes and for the general
        purpose grid, but not otherwise.
    :ivar attachment:
    :ivar points:
    """
    representation_patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationPatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    attachment: Optional[GridGeometryAttachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
