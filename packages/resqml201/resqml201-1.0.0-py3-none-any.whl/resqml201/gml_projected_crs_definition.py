from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_projected_crs import AbstractProjectedCrs
from resqml201.ex_vertical_extent_type import ProjectedCrstype

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GmlProjectedCrsDefinition(AbstractProjectedCrs):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    gml_projected_crs_definition: Optional[ProjectedCrstype] = field(
        default=None,
        metadata={
            "name": "GmlProjectedCrsDefinition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
