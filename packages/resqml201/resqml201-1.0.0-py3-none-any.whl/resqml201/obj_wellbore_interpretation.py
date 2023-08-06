from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjWellboreInterpretation(AbstractFeatureInterpretation):
    """This class contains the data describing an opinion of a borehole.

    This interpretation is relative to one particular well trajectory.

    :ivar is_drilled: Used to indicate that this wellbore has been, or
        is being, drilled. This distinguishes from planned wells. For
        one wellbore feature we may expect to have multiple wellbore
        interpretations: IsDrilled=TRUE for instance will be used for
        updated drilled trajectories. IsDrilled=FALSE for planned
        trajectories.
    """
    class Meta:
        name = "obj_WellboreInterpretation"

    is_drilled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDrilled",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
