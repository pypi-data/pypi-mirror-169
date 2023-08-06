from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.data_object_reference import DataObjectReference
from resqml201.md_reference import MdReference
from resqml201.point3d import Point3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjMdDatum(AbstractResqmlDataObject):
    """Specifies the location of the measured depth = 0 reference point.
    The location of this reference point is defined with respect to a CRS, which need not be the same as the CRS of a wellbore trajectory representation, which may reference this location.

    :ivar location: The location of the md reference point relative to a
        local CRS.
    :ivar md_reference:
    :ivar local_crs:
    """
    class Meta:
        name = "obj_MdDatum"

    location: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    md_reference: Optional[MdReference] = field(
        default=None,
        metadata={
            "name": "MdReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
