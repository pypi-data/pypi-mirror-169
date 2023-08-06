from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.patch import Patch
from resqml201.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DPatch(Patch):
    """Patch representing a single 2D grid and its geometry. The
    FastestAxisCount and the SlowestAxisCount determine the indexing of this
    grid 2D patch, by defining a one dimensional index for the 2D grid as
    follows:

    Index = FastestIndex + FastestAxisCount * SlowestIndex
    This indexing order IS the data order when stored in HDF5, in which case, this would be a SlowestAxisCount*FastestAxisCount two dimensional array in HDF5.

    :ivar fastest_axis_count: The number of nodes in the fastest
        direction.
    :ivar slowest_axis_count: The number of nodes in the slowest
        direction.
    :ivar geometry:
    """
    class Meta:
        name = "Grid2dPatch"

    fastest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FastestAxisCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    slowest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlowestAxisCount",
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
