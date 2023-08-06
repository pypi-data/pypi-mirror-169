from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_activity_parameter import AbstractActivityParameter
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DataObjectParameter(AbstractActivityParameter):
    """
    Parameter referencing to a top level object.

    :ivar data_object: Is actually a reference and not a containment
        relationship.
    """
    data_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
