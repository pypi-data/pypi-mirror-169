from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.patch1d import Patch1D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class EdgePatch(Patch1D):
    """Describes edges that are not linked to any other edge.

    Because edges do not have indices, a consecutive pair of nodes is
    used to identify each edge. The split edges dataset is a set of
    nodes (2 nodes per edge). Each patch has a set of 2 nodes.

    :ivar split_edges: An array of split edges to define patches. It
        points to an HDF5 dataset, which must be a 2D array of non-
        negative integers with dimensions 2 x numSplitEdges. integers
        with dimensions {2, numSplitEdges}
    """
    split_edges: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
