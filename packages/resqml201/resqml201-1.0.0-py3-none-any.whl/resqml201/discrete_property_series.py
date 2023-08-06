from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_discrete_property_series import ObjDiscretePropertySeries

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscretePropertySeries(ObjDiscretePropertySeries):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
