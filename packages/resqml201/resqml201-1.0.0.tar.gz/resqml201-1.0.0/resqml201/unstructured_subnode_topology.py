from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.edges import Edges
from resqml201.nodes_per_cell import NodesPerCell
from resqml201.subnode_topology import SubnodeTopology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredSubnodeTopology(SubnodeTopology):
    """If edge subnodes are used, then edges must be defined.

    If cell subnodes are used, nodes per cell must be defined.
    """
    edges: Optional[Edges] = field(
        default=None,
        metadata={
            "name": "Edges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    nodes_per_cell: Optional[NodesPerCell] = field(
        default=None,
        metadata={
            "name": "NodesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
