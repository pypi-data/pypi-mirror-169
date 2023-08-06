from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.patch import Patch
from resqml201.unstructured_grid_geometry import UnstructuredGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridUnstructuredGridPatch(Patch):
    """Used to specify unstructured cell grid patch(es) within a general
    purpose grid.

    Multiple patches are supported.

    :ivar unstructured_cell_count: Number of unstructured cells.
        Degenerate case (count=0) is allowed for GPGrid.
    :ivar geometry:
    """
    unstructured_cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnstructuredCellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geometry: Optional[UnstructuredGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
