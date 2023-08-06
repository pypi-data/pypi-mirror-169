from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.molar_heat_capacity_uom import MolarHeatCapacityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MolarHeatCapacityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MolarHeatCapacityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
