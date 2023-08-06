from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_value_array import AbstractValueArray
from resqml201.patch import Patch
from resqml201.subnode_node_object import SubnodeNodeObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubnodePatch(Patch):
    """Each patch of subnodes is defined independently of the others.

    Number of nodes per object is determined by the subnode kind.

    :ivar subnode_node_object:
    :ivar node_weights_per_subnode: Node weights for each subnode. Count
        of nodes per subnode is known for each specific subnode
        construction. Data order consists of all the nodes for each
        subnode in turn. For example, if uniform and stored as a multi-
        dimensional array, the node index cycles first. BUSINESS RULE:
        Weights must be non-negative. BUSINESS RULE: Length of array
        must be consistent with the sum of nodeCount x subnodeCount per
        object, e.g., for 3 subnodes per edge (uniform), there are 6
        weights.
    """
    subnode_node_object: Optional[SubnodeNodeObject] = field(
        default=None,
        metadata={
            "name": "SubnodeNodeObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    node_weights_per_subnode: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "NodeWeightsPerSubnode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
