from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerSplitColumnEdges:
    """Column edges are needed to construct the indices for the cell faces for
    column layer grids.

    For split column layer grids, the column edge indices must be
    defined explicitly. Column edges are not required to describe the
    lowest order grid geometry, but may be required for higher order
    geometries or properties.

    :ivar count: Number of split column edges in this grid. Must be
        positive.
    :ivar parent_column_edge_indices: Parent unsplit column edge index
        for each of the split column edges. Used to implicitly define
        split face indexing.
    :ivar column_per_split_column_edge: Column index for each of the
        split column edges. Used to implicitly define column and cell
        faces. List-of-lists construction not required since each split
        column edge must be in a single column.
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_column_edge_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentColumnEdgeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    column_per_split_column_edge: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ColumnPerSplitColumnEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
