from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.linear_acceleration_uom import LinearAccelerationUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LinearAccelerationMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LinearAccelerationUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
