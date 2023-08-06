from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_stratigraphic_unit_feature import ObjStratigraphicUnitFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicUnitFeature(ObjStratigraphicUnitFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
