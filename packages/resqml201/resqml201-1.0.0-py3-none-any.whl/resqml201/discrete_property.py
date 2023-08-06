from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_discrete_property import ObjDiscreteProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteProperty(ObjDiscreteProperty):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
