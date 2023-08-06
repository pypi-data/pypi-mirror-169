from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.patch import Patch
from resqml201.truncation_cell_patch import TruncationCellPatch
from resqml201.unstructured_column_layer_grid_geometry import UnstructuredColumnLayerGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridUnstructuredColumnLayerGridPatch(Patch):
    """Used to specify unstructured column layer grid patch(es) within a
    general purpose grid.

    Multiple patches are supported.

    :ivar unstructured_column_count: Number of unstructured columns.
        Degenerate case (count=0) is allowed for GPGrid.
    :ivar geometry:
    :ivar truncation_cells:
    """
    unstructured_column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
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
