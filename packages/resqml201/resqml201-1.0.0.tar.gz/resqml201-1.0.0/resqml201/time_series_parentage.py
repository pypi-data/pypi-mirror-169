from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TimeSeriesParentage:
    """
    Indicates that a time series has the associated time series as a parent,
    i.e., that the series continues from the parent time series.

    :ivar has_overlap: Used to indicate that a time series overlaps with
        its parent time series, e.g., as may be done for simulation
        studies, where the end state of one calculation is the initial
        state of the next.
    :ivar parent_time_index:
    """
    has_overlap: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasOverlap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "ParentTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
