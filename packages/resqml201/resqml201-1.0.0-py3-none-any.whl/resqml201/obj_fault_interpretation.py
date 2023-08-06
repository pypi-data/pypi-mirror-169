from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.fault_throw import FaultThrow
from resqml201.length_measure import LengthMeasure
from resqml201.obj_boundary_feature_interpretation import ObjBoundaryFeatureInterpretation
from resqml201.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjFaultInterpretation(ObjBoundaryFeatureInterpretation):
    """
    A type of boundary feature, this class contains the data describing an
    opinion about the characterization of the fault, which includes the
    attributes listed below.

    :ivar is_listric: Indicates if the normal fault is listric or not.
        BUSINESS RULE: Must be present if the fault is normal. Must not
        be present if the fault is not normal.
    :ivar maximum_throw:
    :ivar mean_azimuth:
    :ivar mean_dip:
    :ivar throw_interpretation:
    """
    class Meta:
        name = "obj_FaultInterpretation"

    is_listric: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsListric",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    maximum_throw: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumThrow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    mean_azimuth: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanAzimuth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    mean_dip: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanDip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    throw_interpretation: List[FaultThrow] = field(
        default_factory=list,
        metadata={
            "name": "ThrowInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
