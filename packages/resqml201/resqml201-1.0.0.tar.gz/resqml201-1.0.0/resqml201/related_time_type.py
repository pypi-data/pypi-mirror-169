from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.related_time_type_relative_position import RelatedTimeTypeRelativePosition
from resqml201.time_primitive_property_type import TimePrimitivePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    """gml:RelatedTimeType provides a content model for indicating the relative
    position of an arbitrary member of the substitution group whose head is
    gml:AbstractTimePrimitive.

    It extends the generic gml:TimePrimitivePropertyType with an XML
    attribute relativePosition, whose value is selected from the set of
    13 temporal relationships identified by Allen (1983)
    """
    relative_position: Optional[RelatedTimeTypeRelativePosition] = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        }
    )
