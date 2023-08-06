from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class GridGeometryAttachment(Enum):
    """
    Indexable grid elements to which point geometry may be attached to describe
    additional grid geometry.

    :cvar CELLS: Geometry may be attached to cells to distort the
        geometry of that specific cell, only (finite element grid).
    :cvar EDGES: Geometry may be attached to edges to distort the
        geometry of all cells that refer to that edge (finite element
        grid). BUSINESS RULE: The edges indexing must be known or
        defined in the grid representation if geometry is attached to
        the edges.
    :cvar FACES: Geometry may be attached to faces to distort the
        geometry of all cells that refer to that face (finite element
        grid). BUSINESS RULE: The faces indexing must be known or
        defined in the grid representation if geometry is attached to
        the faces.
    :cvar HINGE_NODE_FACES: For column layer grids, these are the K
        faces. For unstructured grids these faces are enumerated as the
        hinge node faces.
    :cvar NODES: Additional grid geometry may be attached to split or
        truncated node patches for column layer grids. All other node
        geometry attachment should be done through the Points array of
        the AbstractGridGeometry, not through the additional grid
        geometry.
    :cvar RADIAL_ORIGIN_POLYLINE: NKL points must be attached to the
        radial origin polyline for a grid with radial interpolation.
        BUSINESS RULE: The optional radialGridIsComplete element must be
        defined in the grid representation if geometry is attached to
        the radial origin polyline.
    :cvar SUBNODES: Geometry may be attached to subnodes to distort the
        geometry of all cells that refer to that subnode (finite element
        grid). BUSINESS RULE: An optional subnode patch object must be
        defined in the grid representation if geometry is attached to
        the subnodes.
    """
    CELLS = "cells"
    EDGES = "edges"
    FACES = "faces"
    HINGE_NODE_FACES = "hinge node faces"
    NODES = "nodes"
    RADIAL_ORIGIN_POLYLINE = "radial origin polyline"
    SUBNODES = "subnodes"
