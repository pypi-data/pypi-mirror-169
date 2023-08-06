from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray
from resqml201.abstract_grid_geometry import AbstractGridGeometry
from resqml201.cell_shape import CellShape
from resqml201.resqml_jagged_array import ResqmlJaggedArray
from resqml201.unstructured_grid_hinge_node_faces import UnstructuredGridHingeNodeFaces
from resqml201.unstructured_subnode_topology import UnstructuredSubnodeTopology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredGridGeometry(AbstractGridGeometry):
    """Description of the geometry of an unstructured cell grid, which includes
    geometric characteristics, e.g., cell face parity, and supporting topology.

    Each grid cell is defined by a (signed) list of cell faces. Each
    cell face is defined by a list of nodes.

    :ivar cell_shape:
    :ivar node_count: Total number of nodes in the grid. Must be
        positive.
    :ivar face_count: Total number of faces in the grid. Must be
        positive.
    :ivar nodes_per_face: List of nodes per face. node count per face
        can be obtained from the offsets in the first list of list
        array. BUSINESS RULE: faceCount must match the length of the
        first list of list array.
    :ivar faces_per_cell: List of faces per cell. face count per cell
        can be obtained from the offsets in the first list of list
        array. BUSINESS RULE: cellCount must match the length of the
        first list of list array.
    :ivar cell_face_is_right_handed: Boolean mask used to indicate which
        cell faces have an outwardly directed normal following a right
        hand rule. Array length is the sum of the cell face count per
        cell, and the data follows the order of the faces per cell
        resqml list-of-lists.
    :ivar hinge_node_faces:
    :ivar subnode_topology:
    """
    cell_shape: Optional[CellShape] = field(
        default=None,
        metadata={
            "name": "CellShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    face_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FaceCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    nodes_per_face: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    faces_per_cell: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "FacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    cell_face_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "CellFaceIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    hinge_node_faces: Optional[UnstructuredGridHingeNodeFaces] = field(
        default=None,
        metadata={
            "name": "HingeNodeFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    subnode_topology: Optional[UnstructuredSubnodeTopology] = field(
        default=None,
        metadata={
            "name": "SubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
