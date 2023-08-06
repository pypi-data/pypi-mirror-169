from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_blocked_wellbore_representation import ObjBlockedWellboreRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BlockedWellboreRepresentation(ObjBlockedWellboreRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
