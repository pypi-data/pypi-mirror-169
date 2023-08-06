from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_continuous_property_series import ObjContinuousPropertySeries

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousPropertySeries(ObjContinuousPropertySeries):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
