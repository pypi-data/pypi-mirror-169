from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_cited_data_object import AbstractCitedDataObject
from resqml201.abstract_projected_crs import AbstractProjectedCrs
from resqml201.axis_order2d import AxisOrder2D
from resqml201.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCrs1(AbstractCitedDataObject):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    class Meta:
        name = "ProjectedCrs"

    axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "AxisOrder",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    abstract_projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "AbstractProjectedCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
