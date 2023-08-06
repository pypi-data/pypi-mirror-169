from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.interval_grid_cells import IntervalGridCells
from resqml201.patch import Patch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StreamlinePolylineSetPatch(Patch):
    """A patch containing a set of polylines. For performance reasons, the
    geometry of each patch is described in only one 1D array of 3D points,
    which aggregates the nodes of all the polylines together. To be able to
    separate the polyline descriptions, additional information is added about
    the type of each polyline (closed or not) and the number of 3D points (node
    count) of each polyline. This additional information is contained in two
    arrays which are associated with each polyline set patch. The dimension of
    these arrays is the number of polylines gathered in one polyline set patch.

    - The first array contains a Boolean for each polyline (closed or not closed)
    - The second array contains the count of nodes for each polyline.

    :ivar node_count: Total number of nodes. BUSINESS RULE: Should be
        equal to the sum of the number of nodes per polyline
    :ivar interval_count: Total number of intervals. BUSINESS RULE:
        Should be equal to the sum of the count of intervals per
        polyline.
    :ivar closed_polylines: Indicates whether a polyline is closed. If
        closed, then the interval count for that polyline is equal to
        the node count. If open, then the interval count for that
        polyline is one less than the node count.
    :ivar node_count_per_polyline: The first number in the list defines
        the node count for the first polyline in the polyline set patch.
        The second number in the list defines the node count for the
        second polyline in the polyline set patch. etc.
    :ivar interval_grid_cells:
    """
    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    interval_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IntervalCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    closed_polylines: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "ClosedPolylines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    node_count_per_polyline: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NodeCountPerPolyline",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    interval_grid_cells: Optional[IntervalGridCells] = field(
        default=None,
        metadata={
            "name": "IntervalGridCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
