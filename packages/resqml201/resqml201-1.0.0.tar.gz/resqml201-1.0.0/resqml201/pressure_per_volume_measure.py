from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.pressure_per_volume_uom import PressurePerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressurePerVolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
