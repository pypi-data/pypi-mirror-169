from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DoubleLookup:
    """
    (key,value) pairs for a lookup table.

    :ivar key: Input to a table lookup.
    :ivar value: Output from a table lookup.
    """
    key: Optional[float] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
