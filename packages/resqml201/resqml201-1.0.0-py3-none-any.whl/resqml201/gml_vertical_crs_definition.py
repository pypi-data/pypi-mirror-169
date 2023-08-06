from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_vertical_crs import AbstractVerticalCrs
from resqml201.ex_vertical_extent_type import VerticalCrstype

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GmlVerticalCrsDefinition(AbstractVerticalCrs):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    gml_vertical_crs_definition: Optional[VerticalCrstype] = field(
        default=None,
        metadata={
            "name": "GmlVerticalCrsDefinition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
