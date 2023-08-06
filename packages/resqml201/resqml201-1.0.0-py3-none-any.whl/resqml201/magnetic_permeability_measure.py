from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.magnetic_permeability_uom import MagneticPermeabilityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticPermeabilityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticPermeabilityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
