from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.ij_split_column_edges import IjSplitColumnEdges
from resqml201.resqml_jagged_array import ResqmlJaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjGaps:
    """
    Optional object used to indicate that adjacent columns of the model are
    split from each other, which is modeled by introducing additional (split)
    pillars.

    :ivar split_pillar_count: Number of split pillars in the model.
        Count must be positive.
    :ivar parent_pillar_indices: Parent pillar index for each of the
        split pillars. This information is used to infer the grid cell
        geometry. BUSINESS RULE: Array length must match
        splitPillarCount.
    :ivar columns_per_split_pillar: List of columns for each of the
        split pillars. This information is used to infer the grid cell
        geometry. BUSINESS RULE: The length of the first list-of-lists
        array must match the splitPillarCount.
    :ivar ij_split_column_edges:
    """
    split_pillar_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SplitPillarCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parent_pillar_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentPillarIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    columns_per_split_pillar: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "ColumnsPerSplitPillar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    ij_split_column_edges: Optional[IjSplitColumnEdges] = field(
        default=None,
        metadata={
            "name": "IjSplitColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
