from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature
from resqml201.seismic_lattice_set_feature import SeismicLatticeSetFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjSeismicLatticeFeature(AbstractSeismicSurveyFeature):
    """Defined by two lateral ordered dimensions: inline (lateral), crossline
    (lateral and orthogonal to the inline dimension), which are fixed.

    To specify its location, a seismic feature can be associated with
    the seismic coordinates of the points of a representation.

    :ivar crossline_count: The count of crosslines in the 3D seismic
        survey.
    :ivar crossline_index_increment: The constant index increment
        between two consecutive crosslines of the 3D seismic survey.
    :ivar first_crossline_index: The index of the first crossline of the
        3D seismic survey.
    :ivar first_inline_index: The index of the first inline of the 3D
        seismic survey.
    :ivar inline_count: The count of inlines in the 3D seismic survey.
    :ivar inline_index_increment: The constant index increment between
        two consecutive inlines of the 3D seismic survey.
    :ivar is_part_of:
    """
    class Meta:
        name = "obj_SeismicLatticeFeature"

    crossline_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CrosslineCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    crossline_index_increment: Optional[int] = field(
        default=None,
        metadata={
            "name": "CrosslineIndexIncrement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    first_crossline_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstCrosslineIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    first_inline_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstInlineIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    inline_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "InlineCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    inline_index_increment: Optional[int] = field(
        default=None,
        metadata={
            "name": "InlineIndexIncrement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    is_part_of: Optional[SeismicLatticeSetFeature] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
