from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_wellbore_marker_frame_representation import ObjWellboreMarkerFrameRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreMarkerFrameRepresentation(ObjWellboreMarkerFrameRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
