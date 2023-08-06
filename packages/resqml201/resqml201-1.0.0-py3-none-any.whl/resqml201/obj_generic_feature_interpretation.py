from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGenericFeatureInterpretation(AbstractFeatureInterpretation):
    class Meta:
        name = "obj_GenericFeatureInterpretation"
