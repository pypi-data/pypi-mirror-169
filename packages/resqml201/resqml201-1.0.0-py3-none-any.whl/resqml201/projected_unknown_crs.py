from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_projected_crs import AbstractProjectedCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedUnknownCrs(AbstractProjectedCrs):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    unknown: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unknown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_length": 1,
            "max_length": 256,
            "white_space": "collapse",
        }
    )
