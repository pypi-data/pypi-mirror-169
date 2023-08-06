from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_activity_template import ObjActivityTemplate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ActivityTemplate(ObjActivityTemplate):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
