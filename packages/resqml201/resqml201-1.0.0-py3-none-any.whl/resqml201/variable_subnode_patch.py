from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.subnode_patch import SubnodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VariableSubnodePatch(SubnodePatch):
    """
    If the number of subnodes per object are variable for each object, use this
    subnode construction.

    :ivar object_indices: Indices of the selected objects
    :ivar subnode_count_per_selected_object: Number of subnodes per
        selected object.
    """
    object_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ObjectIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    subnode_count_per_selected_object: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerSelectedObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
