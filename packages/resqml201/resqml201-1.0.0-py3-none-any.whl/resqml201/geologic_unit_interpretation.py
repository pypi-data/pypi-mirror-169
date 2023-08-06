from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_geologic_unit_interpretation import ObjGeologicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicUnitInterpretation(ObjGeologicUnitInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
