from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_property_set import ObjPropertySet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PropertySet(ObjPropertySet):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
