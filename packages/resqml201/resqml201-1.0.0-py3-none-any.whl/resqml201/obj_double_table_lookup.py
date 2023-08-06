from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_property_lookup import AbstractPropertyLookup
from resqml201.double_lookup import DoubleLookup

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjDoubleTableLookup(AbstractPropertyLookup):
    """Defines a function for table lookups.

    For example, used for linear interpolation, such as PVT. Used for
    categorical property, which also may use StringTableLookup.
    """
    class Meta:
        name = "obj_DoubleTableLookup"

    value: List[DoubleLookup] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
