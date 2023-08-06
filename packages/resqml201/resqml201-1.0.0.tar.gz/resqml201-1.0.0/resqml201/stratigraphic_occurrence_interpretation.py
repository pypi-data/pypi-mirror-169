from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_stratigraphic_occurrence_interpretation import ObjStratigraphicOccurrenceInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicOccurrenceInterpretation(ObjStratigraphicOccurrenceInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
