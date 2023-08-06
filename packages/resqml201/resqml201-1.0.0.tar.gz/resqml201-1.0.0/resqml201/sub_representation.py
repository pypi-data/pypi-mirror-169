from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_sub_representation import ObjSubRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubRepresentation(ObjSubRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
