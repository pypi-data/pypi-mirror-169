from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.resqml_jagged_array import ResqmlJaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NodesPerCell:
    """Optional component of Unstructured Cell Finite Elements.

    The choice of node order per cell is important for effective use of
    the RESQML finite element representations. If you are working with
    an application with a particular node ordering per cell, be sure to
    specify the nodes in that order here, for ease of use. BUSINESS
    RULE: If cell subnodes are used for unstructured grids, then nodes
    per cell must be defined.

    :ivar nodes_per_cell: Defines an ordered list of nodes per cell.
    """
    nodes_per_cell: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
