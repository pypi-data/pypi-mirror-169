from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_geologic_unit_feature import ObjGeologicUnitFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicUnitFeature(ObjGeologicUnitFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
