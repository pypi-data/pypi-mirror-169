from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_horizon_interpretation import ObjHorizonInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HorizonInterpretation(ObjHorizonInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
