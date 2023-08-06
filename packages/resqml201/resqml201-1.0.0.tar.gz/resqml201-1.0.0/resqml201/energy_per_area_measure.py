from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.energy_per_area_uom import EnergyPerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EnergyPerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[EnergyPerAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
