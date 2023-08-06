from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_activity_parameter import AbstractActivityParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StringParameter(AbstractActivityParameter):
    """
    Parameter containing a string value.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
