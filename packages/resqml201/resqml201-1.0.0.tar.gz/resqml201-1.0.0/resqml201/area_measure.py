from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.area_uom import AreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
