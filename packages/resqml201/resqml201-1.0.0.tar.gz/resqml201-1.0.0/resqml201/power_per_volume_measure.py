from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.power_per_volume_uom import PowerPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PowerPerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PowerPerVolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
