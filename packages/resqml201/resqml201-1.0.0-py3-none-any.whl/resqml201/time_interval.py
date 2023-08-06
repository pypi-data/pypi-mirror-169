from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TimeInterval:
    """Geological time during which a geological event (e.g., deposition,
    erosion, fracturation, faulting, intrusion) occurred.

    BUSINESS RULE: All rock features that are present in the global
    chronostratigraphic column feature must have a time interval.
    """
    chrono_bottom: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    chrono_top: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
