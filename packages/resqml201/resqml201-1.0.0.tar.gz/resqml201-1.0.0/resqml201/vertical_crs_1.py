from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_cited_data_object import AbstractCitedDataObject
from resqml201.abstract_vertical_crs import AbstractVerticalCrs
from resqml201.length_uom import LengthUom
from resqml201.vertical_direction import VerticalDirection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalCrs1(AbstractCitedDataObject):
    class Meta:
        name = "VerticalCrs"

    direction: Optional[VerticalDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    abstract_vertical_crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "AbstractVerticalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
