from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.time_series_parentage import TimeSeriesParentage
from resqml201.timestamp import Timestamp

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjTimeSeries(AbstractResqmlDataObject):
    """Stores an ordered list of times, for example, for time-dependent
    properties, geometries, or representations.

    It is used in conjunction with the time index to specify times for
    RESQML.

    :ivar time: Individual times composing the series. The list ordering
        is used by the time index.
    :ivar time_series_parentage:
    """
    class Meta:
        name = "obj_TimeSeries"

    time: List[Timestamp] = field(
        default_factory=list,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
    time_series_parentage: Optional[TimeSeriesParentage] = field(
        default=None,
        metadata={
            "name": "TimeSeriesParentage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
