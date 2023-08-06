from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.data_object_reference import DataObjectReference
from resqml201.length_uom import LengthUom
from resqml201.plane_angle_uom import PlaneAngleUom
from resqml201.point3d import Point3D
from resqml201.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjDeviationSurveyRepresentation(AbstractRepresentation):
    """Specifies the station data from a deviation survey.

    The deviation survey does not provide a complete specification of
    the geometry of a wellbore trajectory. Although a minimum-curvature
    algorithm is used in most cases, the implementation varies
    sufficiently that no single algorithmic specification is available
    as a data transfer standard. Instead, the geometry of a RESQML
    wellbore trajectory is represented by a parametric line,
    parameterized by the MD. CRS and units of measure do not need to be
    consistent with the CRS and units of measure for wellbore trajectory
    representation.

    :ivar witsml_deviation_survey:
    :ivar is_final: Used to indicate that this is a final version of the
        deviation survey, as distinct from the interim interpretations.
    :ivar station_count: Number of Stations
    :ivar md_uom: Units of Measure of the measured depths along this
        deviation survey.
    :ivar mds: MD values for the position of the stations BUSINESS RULE:
        Array length equals station count
    :ivar first_station_location: XYZ location of the first station of
        the deviation survey.
    :ivar angle_uom: Defines the units of measure for the azimuth and
        inclination
    :ivar azimuths: An array of azimuth angles, one for each survey
        station. The rotation is relative to the ProjectedCrs north with
        a positive value indication a clockwise rotation as seen from
        above. If the local CRS - whether a LocalTime3dCrs or a
        LocalDepth3dCrs - is rotated relative to the ProjectedCrs, the
        azimuths remain relative to the ProjectedCrs not the local CRS.
        Note that the projection’s north is not the same as true north
        or magnetic north. A good definition of the different kinds of
        "north" can be found in the OGP Surveying &amp; Positioning
        Guidance Note 1 http://www.ogp.org.uk/pubs/373-01.pdf (the
        "True, Grid and Magnetic North bearings" paragraph). BUSINESS
        RULE: Array length equals station count
    :ivar inclinations: Dip (or inclination) angle for each station.
        BUSINESS RULE: Array length equals station count
    :ivar md_datum:
    :ivar time_index:
    """
    class Meta:
        name = "obj_DeviationSurveyRepresentation"

    witsml_deviation_survey: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlDeviationSurvey",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    is_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFinal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    station_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "StationCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    md_uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "name": "MdUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    mds: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "Mds",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    first_station_location: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "FirstStationLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    angle_uom: Optional[PlaneAngleUom] = field(
        default=None,
        metadata={
            "name": "AngleUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    azimuths: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "Azimuths",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    inclinations: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "Inclinations",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    md_datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MdDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
