from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_object_type import AbstractObjectType
from resqml201.boolean_property_type import BooleanPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractExGeographicExtentType(AbstractObjectType):
    """
    Geographic area of the dataset.
    """
    class Meta:
        name = "AbstractEX_GeographicExtent_Type"

    extent_type_code: Optional[BooleanPropertyType] = field(
        default=None,
        metadata={
            "name": "extentTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
