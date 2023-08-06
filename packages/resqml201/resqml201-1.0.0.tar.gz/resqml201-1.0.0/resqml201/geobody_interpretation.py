from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_geobody_interpretation import ObjGeobodyInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeobodyInterpretation(ObjGeobodyInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
