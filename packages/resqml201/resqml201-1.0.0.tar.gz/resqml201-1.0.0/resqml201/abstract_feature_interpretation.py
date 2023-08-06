from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.data_object_reference import DataObjectReference
from resqml201.domain import Domain
from resqml201.time_interval import TimeInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractFeatureInterpretation(AbstractResqmlDataObject):
    """
    The main class that contains all of the other feature interpretations
    included in this interpreted model.
    """
    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Domain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    interpreted_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InterpretedFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    has_occured_during: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "name": "HasOccuredDuring",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
