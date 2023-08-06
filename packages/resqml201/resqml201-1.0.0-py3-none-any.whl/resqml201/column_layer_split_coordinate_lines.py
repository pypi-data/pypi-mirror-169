from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.column_layer_split_column_edges import ColumnLayerSplitColumnEdges
from resqml201.resqml_jagged_array import ResqmlJaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerSplitCoordinateLines:
    """Definition of the indexing for the split coordinate lines.

    When present, this indexing contributes to the coordinate line
    nodes.

    :ivar count: Number of split coordinate lines. The count must be
        positive.
    :ivar pillar_indices: Pillar index for each split coordinate line.
        Length of this array is equal to the number of split coordinate
        lines. For the first pillarCount lines, the index of the
        coordinate line equals the index of the corresponding pillar.
        This array provides the pillar indices for the additional
        (split) coordinate lines. Used to implicitly define column and
        cell geometry.
    :ivar columns_per_split_coordinate_line: Column indices for each of
        the split coordinate lines. Used to implicitly define column and
        cell geometry. List-of-lists construction used to support shared
        coordinate lines.
    :ivar split_column_edges:
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
    pillar_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "PillarIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    columns_per_split_coordinate_line: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "ColumnsPerSplitCoordinateLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    split_column_edges: Optional[ColumnLayerSplitColumnEdges] = field(
        default=None,
        metadata={
            "name": "SplitColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
