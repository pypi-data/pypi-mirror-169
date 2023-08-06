from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_wellbore_frame_representation import ObjWellboreFrameRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreFrameRepresentation(ObjWellboreFrameRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
