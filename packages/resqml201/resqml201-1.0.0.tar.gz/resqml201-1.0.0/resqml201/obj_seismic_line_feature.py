from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjSeismicLineFeature(AbstractSeismicSurveyFeature):
    """Defined by one lateral dimension: trace (lateral).

    Seismic trace of the 3D seismic survey. To specify its location, the
    seismic feature can be associated with the seismic coordinates of
    the points of a representation.

    :ivar first_trace_index: The index of the first trace of the seismic
        line.
    :ivar trace_count: The count of traces in the seismic line.
    :ivar trace_index_increment: The constant index increment between
        two consecutive traces.
    :ivar is_part_of:
    """
    class Meta:
        name = "obj_SeismicLineFeature"

    first_trace_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstTraceIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    trace_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TraceCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    trace_index_increment: Optional[int] = field(
        default=None,
        metadata={
            "name": "TraceIndexIncrement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    is_part_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
