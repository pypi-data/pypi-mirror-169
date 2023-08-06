from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.edge_patch import EdgePatch
from resqml201.patch1d import Patch1D
from resqml201.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TrianglePatch(Patch1D):
    """Patch made of triangles, where the number of triangles is given by the
    patch count. BUSINESS RULE: Within a patch, all the triangles must be
    contiguous. The patch contains:

    - Number of nodes within the triangulation and their locations.
    - 2D array describing the topology of the triangles.
    Two triangles that are connected may be in different patches.

    :ivar node_count:
    :ivar triangles: The triangles are a 2D array of non-negative
        integers with the dimensions 3 x numTriangles.
    :ivar geometry:
    :ivar split_edge_patch:
    """
    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    triangles: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Triangles",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    split_edge_patch: List[EdgePatch] = field(
        default_factory=list,
        metadata={
            "name": "SplitEdgePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
