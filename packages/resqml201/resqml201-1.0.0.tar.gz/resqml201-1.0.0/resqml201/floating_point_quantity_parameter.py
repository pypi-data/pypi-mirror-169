from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_activity_parameter import AbstractActivityParameter
from resqml201.resqml_uom import ResqmlUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FloatingPointQuantityParameter(AbstractActivityParameter):
    """
    Parameter containing a double value.

    :ivar value: Double value
    :ivar uom: Unit of measure associated with the value
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    uom: Optional[ResqmlUom] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
