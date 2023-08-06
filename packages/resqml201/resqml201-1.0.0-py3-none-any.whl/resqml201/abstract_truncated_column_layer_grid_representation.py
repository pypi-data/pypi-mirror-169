from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_grid_representation import AbstractGridRepresentation
from resqml201.truncation_cell_patch import TruncationCellPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractTruncatedColumnLayerGridRepresentation(AbstractGridRepresentation):
    """Abstract class for truncated IJK grids and truncated unstructured column
    layer grids.

    Each column layer grid class must have a defined geometry in which
    cells are truncated and additional split cells are defined.

    :ivar nk: Number of layers in the grid. Must be positive.
    :ivar truncation_cells:
    """
    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    truncation_cells: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
