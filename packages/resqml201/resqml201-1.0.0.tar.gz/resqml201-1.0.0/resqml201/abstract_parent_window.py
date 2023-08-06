from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.cell_overlap import CellOverlap

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractParentWindow:
    """Parent window specification, organized according to the topology of the
    parent grid.

    In addition to a window specification, for grids with I, J, and/or K
    coordinates, the parentage construction includes a regridding
    description that covers grid refinement, coarsening, or any
    combination of the two.
    """
    cell_overlap: Optional[CellOverlap] = field(
        default=None,
        metadata={
            "name": "CellOverlap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
