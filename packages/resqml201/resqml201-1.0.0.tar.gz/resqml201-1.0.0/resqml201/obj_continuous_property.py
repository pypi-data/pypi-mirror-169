from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_values_property import AbstractValuesProperty
from resqml201.resqml_uom import ResqmlUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjContinuousProperty(AbstractValuesProperty):
    """Most common type of property used for storing rock or fluid attributes;
    all are represented as doubles.

    So that the value range can be known before accessing all values,
    the min and max values of the range are also stored. BUSINESS RULE:
    It also contains a unit of measure that can be different from the
    unit of measure of its property type, but it must be convertible
    into this unit.

    :ivar minimum_value: The minimum of the associated property values.
        BUSINESS RULE: There can be only one value per number of
        elements.
    :ivar maximum_value: The maximum of the associated property values.
        BUSINESS RULE: There can be only one value per number of
        elements.
    :ivar uom: Unit of measure for the property.
    """
    class Meta:
        name = "obj_ContinuousProperty"

    minimum_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    maximum_value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    uom: Optional[ResqmlUom] = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
