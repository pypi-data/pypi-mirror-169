from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_time_series import ObjTimeSeries

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TimeSeries(ObjTimeSeries):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
