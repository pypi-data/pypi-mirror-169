from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Intervals:
    """Refinement and/or Coarsening per interval.

    If there is a 1:1 correspondence between the parent and child cells,
    then this object is not needed.

    :ivar interval_count: The number of intervals in the regrid
        description. Must be positive.
    :ivar parent_count_per_interval: The number of parent cells in each
        interval. BUSINESS RULES: 1.) The array length must be equal to
        intervalCount. 2.) For the given parentIndex, the total count of
        parent cells should not extend beyond the boundary of the parent
        grid.
    :ivar child_count_per_interval: The number of child cells in each
        interval. If the child grid type is not commensurate with the
        parent type, then this attribute is ignored by a reader, and its
        value should be set to null (-1). For example, for a parent IJK
        grid with a child unstructured column layer grid, then the child
        count is non-null for a K regrid, but null for an I or J regrid.
        BUSINESS RULES: 1.) The array length must be equal to
        intervalCount. 2.) If the child grid type is commensurate with
        the parent grid, then the sum of values over all intervals must
        be equal to the corresponding child grid dimension.
    :ivar child_cell_weights: Weights that are proportional to the
        relative sizes of child cells within each interval. The weights
        need not be normalized.
    """
    interval_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IntervalCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_count_per_interval: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentCountPerInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    child_count_per_interval: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ChildCountPerInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    child_cell_weights: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "ChildCellWeights",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
