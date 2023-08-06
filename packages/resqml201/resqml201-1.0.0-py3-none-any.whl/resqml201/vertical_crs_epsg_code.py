from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_vertical_crs import AbstractVerticalCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalCrsEpsgCode(AbstractVerticalCrs):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    epsg_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "EpsgCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
