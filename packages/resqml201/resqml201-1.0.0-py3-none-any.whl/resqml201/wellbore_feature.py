from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_wellbore_feature import ObjWellboreFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreFeature(ObjWellboreFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
