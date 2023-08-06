from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_stratigraphic_unit_interpretation import ObjStratigraphicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicUnitInterpretation(ObjStratigraphicUnitInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
