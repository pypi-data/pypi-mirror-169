from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.temperature_interval_uom import TemperatureIntervalUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TemperatureIntervalMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[TemperatureIntervalUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
