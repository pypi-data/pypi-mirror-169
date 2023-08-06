from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_deviation_survey_representation import ObjDeviationSurveyRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DeviationSurveyRepresentation(ObjDeviationSurveyRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
