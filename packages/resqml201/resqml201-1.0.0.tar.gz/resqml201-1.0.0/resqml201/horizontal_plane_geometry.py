from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_plane_geometry import AbstractPlaneGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HorizontalPlaneGeometry(AbstractPlaneGeometry):
    """
    Defines the infinite geometry of a horizontal plane provided by giving its
    unique Z value.
    """
    coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
