from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.patch1d import Patch1D
from resqml201.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NodePatch(Patch1D):
    """
    Patch representing a list of nodes to which geometry may be attached.
    """
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
