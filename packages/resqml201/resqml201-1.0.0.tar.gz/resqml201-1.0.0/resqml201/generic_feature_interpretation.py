from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_generic_feature_interpretation import ObjGenericFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GenericFeatureInterpretation(ObjGenericFeatureInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
