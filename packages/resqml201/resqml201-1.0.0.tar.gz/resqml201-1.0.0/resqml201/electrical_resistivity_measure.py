from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.electrical_resistivity_uom import ElectricalResistivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricalResistivityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricalResistivityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
