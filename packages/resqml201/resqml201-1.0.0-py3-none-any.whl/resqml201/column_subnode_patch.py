from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.subnode_patch import SubnodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnSubnodePatch(SubnodePatch):
    """
    Use this subnode construction if the number of subnodes per object varies
    from column to column, but does not vary from layer to layer.

    :ivar subnode_count_per_object: Number of subnodes per object, with
        a different number in each column of the grid.
    """
    subnode_count_per_object: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
