from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.data_object_reference import DataObjectReference
from resqml201.resqml_jagged_array import ResqmlJaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ConnectionInterpretations:
    """
    :ivar interpretation_indices: Indices for the interpretations for
        each connection, if any. The use of a Resqml jagged array allows
        zero or more than one interpretation to be associated with a
        single connection.
    :ivar feature_interpretation:
    """
    interpretation_indices: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "InterpretationIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    feature_interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FeatureInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
