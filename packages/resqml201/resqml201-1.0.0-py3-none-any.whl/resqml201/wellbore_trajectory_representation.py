from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_wellbore_trajectory_representation import ObjWellboreTrajectoryRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreTrajectoryRepresentation(ObjWellboreTrajectoryRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
