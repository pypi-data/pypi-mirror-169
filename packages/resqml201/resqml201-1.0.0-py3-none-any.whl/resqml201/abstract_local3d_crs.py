from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_projected_crs import AbstractProjectedCrs
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.abstract_vertical_crs import AbstractVerticalCrs
from resqml201.axis_order2d import AxisOrder2D
from resqml201.length_uom import LengthUom
from resqml201.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractLocal3DCrs(AbstractResqmlDataObject):
    """Defines a local 2D+1D coordinate reference system, by translation and
    rotation, whose origin is located at the (X,Y,Z) Offset from the Projected
    and Vertical 2D+1D CRS. The units of measure in XY follow the Projected
    Crs. The units of measure of the third coordinate is determined in the
    depth or concrete type. ArealRotation is a plane angle. Defines a local 3D
    CRS is subject to the following restrictions:

    - The projected 2d CRS must have orthogonal axes
    - The vertical 1d CRS must be chosen so that it is orthogonal to the plane defined by the projected 2d CRS
    As a consequence of the definition:
    - The local CRS forms a Cartesian system of axes.
    - The local areal axes are in the plane of the projected system.
    - The local areal axes are orthogonal to each other.
    This 3D system is semantically equivalent to a compound CRS composed of a local 2D areal system and a local 1D vertical system.
    The labels associated with the axes on this local system are X, Y, Z or X, Y, T.
    The relative orientation of the local Y axis with respect to the local X axis is identical to that of the global axes.

    :ivar yoffset: The Y offset of the origin of the local areal axes
        relative to the projected CRS origin. The value MUST represent
        the second axis of the coordinate system. The unit of measure is
        defined by the unit of measure for the projected 2D CRS.
    :ivar zoffset: The Z offset of the origin of the local vertical axis
        relative to the vertical CRS origin. According to CRS type
        (depth or time) it corresponds to the depth or time datum The
        value MUST represent the third axis of the coordinate system.
        The unit of measure is defined by the unit of measure for the
        vertical CRS.
    :ivar areal_rotation: The rotation of the local Y axis relative to
        the projected Y axis. - A positive value indicates a clockwise
        rotation from the projected Y axis. - A negative value indicates
        a counter-clockwise rotation form the projected Y axis.
    :ivar projected_axis_order: Defines the coordinate system axis order
        of the global projected CRS when the projected CRS is an unknown
        CRS, else it must be correspond to the axis order of the
        projected  CRS.
    :ivar projected_uom: Unit of measure of the associated Projected
        CRS. When the projected CRS is not unknown, it must be the same
        than the unit defined by the Projected CRS.
    :ivar vertical_uom: Unit of measure of the associated Vertical CRS.
        When the vertical CRS is not unknown, it must be the same than
        the unit defined by the Vertical CRS.
    :ivar xoffset: The X location of the origin of the local areal axes
        relative to the projected CRS origin. The value MUST represent
        the first axis of the coordinate system. The unit of measure is
        defined by the unit of measure for the projected 2D CRS.
    :ivar zincreasing_downward: Indicates that Z values correspond to
        depth values and are increasing downward, as opposite to
        elevation values increasing upward. When the vertical CRS is not
        an unknown, it must correspond to the axis orientation of the
        vertical CRS.
    :ivar vertical_crs:
    :ivar projected_crs:
    """
    class Meta:
        name = "AbstractLocal3dCrs"

    yoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "YOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    zoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "ZOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    areal_rotation: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "ArealRotation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "ProjectedAxisOrder",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "name": "ProjectedUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    vertical_uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "name": "VerticalUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    xoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "XOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    zincreasing_downward: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZIncreasingDownward",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    vertical_crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
