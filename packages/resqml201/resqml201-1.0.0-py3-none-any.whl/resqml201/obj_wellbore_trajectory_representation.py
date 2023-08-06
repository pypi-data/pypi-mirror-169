from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_parametric_line_geometry import AbstractParametricLineGeometry
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.data_object_reference import DataObjectReference
from resqml201.length_uom import LengthUom
from resqml201.md_domain import MdDomain
from resqml201.wellbore_trajectory_parent_intersection import WellboreTrajectoryParentIntersection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjWellboreTrajectoryRepresentation(AbstractRepresentation):
    """
    Representation of a wellbore trajectory.

    :ivar start_md: Specifies the measured depth  for the start of the
        wellbore trajectory. Range may often be from kickoff to TD, but
        this is not necessary. BUSINESS RULE: Start MD is always less
        than the Finish MD.
    :ivar finish_md: Specifies the ending measured depth of the range
        for the wellbore trajectory. Range may often be from kickoff to
        TD, but this is not necessary. BUSINESS RULE: Start MD is always
        less than the Finish MD.
    :ivar md_uom: The unit of measure of the reference MD.
    :ivar md_domain:
    :ivar witsml_trajectory: Pointer to the WITSML trajectory that is
        contained in the referenced wellbore. (For information about
        WITSML well and wellbore references, see the definition for
        RESQML technical feature, WellboreFeature).
    :ivar geometry: Explicit geometry is not required for vertical wells
    :ivar md_datum:
    :ivar deviation_survey:
    :ivar parent_intersection:
    """
    class Meta:
        name = "obj_WellboreTrajectoryRepresentation"

    start_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    finish_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "FinishMd",
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
    md_domain: Optional[MdDomain] = field(
        default=None,
        metadata={
            "name": "MdDomain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    witsml_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlTrajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geometry: Optional[AbstractParametricLineGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
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
    deviation_survey: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DeviationSurvey",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parent_intersection: Optional[WellboreTrajectoryParentIntersection] = field(
        default=None,
        metadata={
            "name": "ParentIntersection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
