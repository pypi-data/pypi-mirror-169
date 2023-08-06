from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.obj_wellbore_frame_representation import ObjWellboreFrameRepresentation
from resqml201.wellbore_marker import WellboreMarker

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjWellboreMarkerFrameRepresentation(ObjWellboreFrameRepresentation):
    """
    A well log frame where each entry represents a well marker.
    """
    class Meta:
        name = "obj_WellboreMarkerFrameRepresentation"

    wellbore_marker: List[WellboreMarker] = field(
        default_factory=list,
        metadata={
            "name": "WellboreMarker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
