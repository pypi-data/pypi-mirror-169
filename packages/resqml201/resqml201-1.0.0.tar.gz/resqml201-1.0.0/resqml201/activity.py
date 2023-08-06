from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_activity import ObjActivity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Activity(ObjActivity):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
