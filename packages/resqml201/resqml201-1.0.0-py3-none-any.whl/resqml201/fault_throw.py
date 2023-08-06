from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.throw_kind import ThrowKind
from resqml201.time_interval import TimeInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FaultThrow:
    """
    Identifies the characteristic of the throw of a fault interpretation.
    """
    throw: List[ThrowKind] = field(
        default_factory=list,
        metadata={
            "name": "Throw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
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
