from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_local3d_crs import AbstractLocal3DCrs
from resqml201.time_uom import TimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjLocalTime3DCrs(AbstractLocal3DCrs):
    """Defines a local time coordinate system, the geometrical origin and
    location is defined by the elements of the base class AbstractLocal3dCRS.

    This CRS defines the time unit that the time-based geometries that
    refers it will use.

    :ivar time_uom: Defines the unit of measure of the third (time)
        coordinates, for the geometries that refers to it.
    """
    class Meta:
        name = "obj_LocalTime3dCrs"

    time_uom: Optional[TimeUom] = field(
        default=None,
        metadata={
            "name": "TimeUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
