from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray
from resqml201.abstract_grid_geometry import AbstractGridGeometry
from resqml201.column_layer_split_coordinate_lines import ColumnLayerSplitCoordinateLines
from resqml201.column_layer_subnode_topology import ColumnLayerSubnodeTopology
from resqml201.kdirection import Kdirection
from resqml201.pillar_shape import PillarShape
from resqml201.split_node_patch import SplitNodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractColumnLayerGridGeometry(AbstractGridGeometry):
    """Description of the geometry of a column layer grid, e.g., parity and
    pinch, together with its supporting topology.

    Column layer grid cell geometry is based upon nodes on coordinate
    lines. Geometry is contained within the representation of a grid.
    Point Geometry is that of the column layer coordinate line nodes.
    Coordinate line nodes for all of the coordinate lines, with NKL
    nodes per line. The numbering of these lines follow the pillar
    numbering if no split coordinate lines are present. The unsplit
    coordinate lines share an indexing with the pillars. The numbering
    of the remaining lines are defined in the
    columnsPerSplitCoordinateLine list-of-lists if split coordinate
    lines are present. Pillar numbering is either 1D or 2D, so for
    unfaulted grids, the node dimensions may follow either a 2D or 3D
    array. Otherwise the nodes will be 2D. In HDF5 nodes are stored as
    separate X, Y, Z, values, so add another dimension (size=3) which is
    fastest in HDF5.

    :ivar kdirection:
    :ivar pillar_geometry_is_defined: Indicator that a pillar has at
        least one node with a defined cell geometry. This is considered
        grid meta-data. If the indicator does not indicate that the
        pillar geometry is defined, then this over-rides any other node
        geometry specification. Array index follows #Pillars and so may
        be either 2d or 1d.
    :ivar pillar_shape:
    :ivar cell_geometry_is_defined: Indicator that a cell has a defined
        geometry. This attribute is grid metadata. If the indicator
        shows that the cell geometry is NOT defined, then this attribute
        overrides any other node geometry specification. Array index is
        2D/3D.
    :ivar node_is_colocated_in_kdirection: Optional indicator that two
        adjacent nodes on a coordinate line are colocated. This is
        considered grid meta-data, and is intended to over-ride any
        geometric comparison of node locations. Array index follows
        #CoordinateLines x (NKL-1).
    :ivar node_is_colocated_on_kedge: Optional indicator that two
        adjacent nodes on the KEDGE of a cell are colocated. This is
        considered grid meta-data, and is intended to over-ride any
        geometric comparison of node locations. Array index follows
        #EdgesPerColumn x NKL for unstructured column layer grids and 4
        x NI x NJ x NKL for IJK grids.
    :ivar subnode_topology:
    :ivar split_coordinate_lines:
    :ivar split_nodes:
    """
    kdirection: Optional[Kdirection] = field(
        default=None,
        metadata={
            "name": "KDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillar_geometry_is_defined: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "PillarGeometryIsDefined",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillar_shape: Optional[PillarShape] = field(
        default=None,
        metadata={
            "name": "PillarShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    cell_geometry_is_defined: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "CellGeometryIsDefined",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    node_is_colocated_in_kdirection: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "NodeIsColocatedInKDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    node_is_colocated_on_kedge: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "NodeIsColocatedOnKEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    subnode_topology: Optional[ColumnLayerSubnodeTopology] = field(
        default=None,
        metadata={
            "name": "SubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    split_coordinate_lines: Optional[ColumnLayerSplitCoordinateLines] = field(
        default=None,
        metadata={
            "name": "SplitCoordinateLines",
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
