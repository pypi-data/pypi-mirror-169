from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.area_per_time_uom import AreaPerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaPerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AreaPerTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
