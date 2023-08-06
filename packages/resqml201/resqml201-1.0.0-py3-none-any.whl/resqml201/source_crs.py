from __future__ import annotations
from dataclasses import dataclass
from resqml201.crsproperty_type import CrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SourceCrs(CrspropertyType):
    """
    gml:sourceCRS is an association role to the source CRS (coordinate
    reference system) of this coordinate operation.
    """
    class Meta:
        name = "sourceCRS"
        namespace = "http://www.opengis.net/gml/3.2"
