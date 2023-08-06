from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjBoundaryFeatureInterpretation(AbstractFeatureInterpretation):
    """The main class for data describing an opinion of a surface feature
    between two volumes.

    BUSINESS RULE: The data-object reference (of type "interprets") must
    reference only a boundary feature.
    """
    class Meta:
        name = "obj_BoundaryFeatureInterpretation"
