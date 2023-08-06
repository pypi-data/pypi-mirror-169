from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_grid_representation import AbstractGridRepresentation
from resqml201.unstructured_grid_geometry import UnstructuredGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjUnstructuredGridRepresentation(AbstractGridRepresentation):
    """Unstructured grid representation characterized by a cell count, and
    potentially nothing else.

    Both the oldest and newest simulation formats are based on this
    format.

    :ivar cell_count: Number of cells in the grid. Must be positive.
    :ivar geometry:
    """
    class Meta:
        name = "obj_UnstructuredGridRepresentation"

    cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellCount",
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
