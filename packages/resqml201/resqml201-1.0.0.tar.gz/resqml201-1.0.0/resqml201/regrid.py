from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.intervals import Intervals

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Regrid:
    """One-dimensional I, J, or K refinement and coarsening regrid
    specification.

    The regrid description is organized using intervals. Within each
    interval, the number of parent and child cells is specified. Parent
    and child grid cell faces are aligned at interval boundaries. By
    default, child cells are uniformly sized within an interval unless
    weights are used to modify their size. If the child grid is a root
    grid with an independent geometry, then there will usually be only a
    single interval for a regrid, because internal cell faces are not
    necessarily aligned.

    :ivar initial_index_on_parent_grid: 0-based index for the placement
        of the window on the parent grid.
    :ivar intervals:
    """
    initial_index_on_parent_grid: Optional[int] = field(
        default=None,
        metadata={
            "name": "InitialIndexOnParentGrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "name": "Intervals",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
