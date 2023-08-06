from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_earth_model_interpretation import ObjEarthModelInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class EarthModelInterpretation(ObjEarthModelInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
