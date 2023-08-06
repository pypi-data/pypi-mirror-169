from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractIntegerArray(AbstractValueArray):
    """Generic representation of an array of integer values.

    Each derived element provides specialized implementation to allow
    specific optimization of the representation.
    """
