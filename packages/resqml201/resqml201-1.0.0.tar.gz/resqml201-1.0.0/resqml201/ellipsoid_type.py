from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.identified_object_type import IdentifiedObjectType
from resqml201.second_defining_parameter_2 import SecondDefiningParameter2

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidType(IdentifiedObjectType):
    semi_major_axis: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    second_defining_parameter: Optional[SecondDefiningParameter2] = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
