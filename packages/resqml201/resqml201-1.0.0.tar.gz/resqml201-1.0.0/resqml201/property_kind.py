from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_property_kind import ObjPropertyKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PropertyKind(ObjPropertyKind):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
