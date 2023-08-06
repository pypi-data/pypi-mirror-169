from __future__ import annotations
from dataclasses import dataclass
from resqml201.crsproperty_type import CrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TargetCrs(CrspropertyType):
    """
    gml:targetCRS is an association role to the target CRS (coordinate
    reference system) of this coordinate operation.
    """
    class Meta:
        name = "targetCRS"
        namespace = "http://www.opengis.net/gml/3.2"
