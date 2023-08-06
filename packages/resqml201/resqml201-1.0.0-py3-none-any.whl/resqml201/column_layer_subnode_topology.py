from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.column_subnode_patch import ColumnSubnodePatch
from resqml201.subnode_topology import SubnodeTopology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerSubnodeTopology(SubnodeTopology):
    """
    This data-object consists of the Unstructured Cell Finite Elements subnode
    topology plus the column subnodes.
    """
    column_subnodes: List[ColumnSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "ColumnSubnodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
