from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.column_layer_split_column_edges import ColumnLayerSplitColumnEdges
from resqml201.column_layer_subnode_topology import ColumnLayerSubnodeTopology
from resqml201.ij_split_column_edges import IjSplitColumnEdges
from resqml201.split_edges import SplitEdges
from resqml201.split_faces import SplitFaces
from resqml201.split_node_patch import SplitNodePatch
from resqml201.unstructured_column_edges import UnstructuredColumnEdges
from resqml201.unstructured_subnode_topology import UnstructuredSubnodeTopology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AdditionalGridTopology:
    """Additional grid topology and/or patches, if required, for indexable
    elements that otherwise do not have their topology defined within the grid
    representation.

    For example, column edges need to be defined if we wish to have an
    enumeration for the faces of a column layer grid, but not otherwise.
    """
    split_edges: Optional[SplitEdges] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    split_nodes: Optional[SplitNodePatch] = field(
        default=None,
        metadata={
            "name": "SplitNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
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
    unstructured_column_edges: Optional[UnstructuredColumnEdges] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    split_faces: Optional[SplitFaces] = field(
        default=None,
        metadata={
            "name": "SplitFaces",
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
    unstructured_subnode_topology: Optional[UnstructuredSubnodeTopology] = field(
        default=None,
        metadata={
            "name": "UnstructuredSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    column_layer_subnode_topology: Optional[ColumnLayerSubnodeTopology] = field(
        default=None,
        metadata={
            "name": "ColumnLayerSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
