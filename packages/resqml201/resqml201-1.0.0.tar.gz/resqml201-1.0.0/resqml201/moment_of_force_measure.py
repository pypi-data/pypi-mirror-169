from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.moment_of_force_uom import MomentOfForceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MomentOfForceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MomentOfForceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
