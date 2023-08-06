from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GreenwichLongitude:
    """gml:greenwichLongitude is the longitude of the prime meridian measured
    from the Greenwich meridian, positive eastward.

    If the value of the prime meridian "name" is "Greenwich" then the
    value of greenwichLongitude shall be 0 degrees.
    """
    class Meta:
        name = "greenwichLongitude"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
