from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TimeIndices:
    """Indices into a time series.

    Used to specify time. (Not to be confused with time step.)

    :ivar time_index_count:
    :ivar time_index_start: The index of the start time in the time
        series, if not zero.
    :ivar simulator_time_step: Simulation time step for each time index
    :ivar use_interval: When UseInterval is true, the values are
        associated with each time intervals between two consecutive time
        entries instead of each individual time entry. As a consequence
        the dimension of the value array corresponding to the time
        series is the number of entry in the series minus one.
    :ivar time_series:
    """
    time_index_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeIndexCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time_index_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeIndexStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    simulator_time_step: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SimulatorTimeStep",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    use_interval: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time_series: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
