from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.molecular_weight_uom import MolecularWeightUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MolecularWeightMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MolecularWeightUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
