from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.ijk_grid_geometry import IjkGridGeometry
from resqml201.patch import Patch
from resqml201.truncation_cell_patch import TruncationCellPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridIjkGridPatch(Patch):
    """Used to specify IJK grid patch(es) within a general purpose grid.

    Multiple patches are supported.

    :ivar ni: Count of I indices. Degenerate case (ni=0) is allowed for
        GPGrid representations.
    :ivar nj: Count of J indices. Degenerate case (nj=0) is allowed for
        GPGrid representations.
    :ivar radial_grid_is_complete: TRUE if the grid is periodic in J,
        i.e., has the topology of a complete 360 degree circle. If TRUE,
        then NJL=NJ. Otherwise, NJL=NJ+1
    :ivar geometry:
    :ivar truncation_cells:
    """
    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    radial_grid_is_complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RadialGridIsComplete",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    truncation_cells: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
