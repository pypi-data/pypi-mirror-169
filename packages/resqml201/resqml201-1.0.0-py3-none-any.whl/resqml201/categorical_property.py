from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_categorical_property import ObjCategoricalProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CategoricalProperty(ObjCategoricalProperty):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
