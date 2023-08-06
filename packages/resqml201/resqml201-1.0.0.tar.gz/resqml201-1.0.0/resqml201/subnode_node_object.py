from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class SubnodeNodeObject(Enum):
    """SubnodeNodeObject is used to specify the node object that supports the
    subnodes.

    This determines the number of nodes per subnode and the continuity
    of the associated geometry or property. For instance, for hexahedral
    cells, cell indicates a fixed value of 8, while for an unstructured
    column layer grid, cell indicates that this count varies from column
    to column.

    :cvar CELL: If geometry or properties are discontinuous from cell to
        cell (i.e., their spatial support is cell), then attach them to
        cell subnodes. BUSINESS RULE: If this object kind is selected,
        then an ordered list of nodes per cell must be specified or
        otherwise known.
    :cvar FACE: If geometry or properties are continuous between cells
        that share the same face (i.e., their spatial support is the
        face), then attach them to face subnodes. BUSINESS RULE: If this
        object kind is selected, then an ordered list of nodes per face
        must be specified or otherwise known.
    :cvar EDGE: If geometry and properties are continuous between cells
        that share the same edge of a face (i.e. their spatial support
        is the edge), then attach them to edge subnodes. BUSINESS RULE:
        If this object kind is selected, then an ordered list of nodes
        per edge must be specified or otherwise known.
    """
    CELL = "cell"
    FACE = "face"
    EDGE = "edge"
