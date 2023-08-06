from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_property_lookup import AbstractPropertyLookup
from resqml201.string_lookup import StringLookup

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStringTableLookup(AbstractPropertyLookup):
    """Defines an integer-to-string lookup table, for example, stores facies properties, where a facies index is associated with a facies name. .
    Used for categorical properties, which also may use a double table lookup."""
    class Meta:
        name = "obj_StringTableLookup"

    value: List[StringLookup] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
