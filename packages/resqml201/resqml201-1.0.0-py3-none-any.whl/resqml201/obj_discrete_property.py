from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_values_property import AbstractValuesProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjDiscreteProperty(AbstractValuesProperty):
    """Contains discrete integer values; typically used to store any type of
    index.

    So that the value range can be known before accessing all values, it
    also stores the minimum and maximum value in the range.

    :ivar minimum_value: The minimum of the associated property values.
        BUSINESS RULE: There can only be one value per number of
        elements.
    :ivar maximum_value: The maximum of the associated property values.
        BUSINESS RULE: There can only be one value per number of
        elements.
    """
    class Meta:
        name = "obj_DiscreteProperty"

    minimum_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    maximum_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
