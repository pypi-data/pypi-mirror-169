from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3D:
    """
    Defines a point using coordinates in 3D space.

    :ivar coordinate1: X Coordinate
    :ivar coordinate2: Y Coordinate
    :ivar coordinate3: Either Z or T Coordinate
    """
    class Meta:
        name = "Point3d"

    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    coordinate3: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
