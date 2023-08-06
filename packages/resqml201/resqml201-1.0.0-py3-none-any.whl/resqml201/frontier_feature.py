from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_frontier_feature import ObjFrontierFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FrontierFeature(ObjFrontierFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
