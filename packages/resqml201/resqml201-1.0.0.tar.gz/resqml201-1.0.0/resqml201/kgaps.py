from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Kgaps:
    """Optional object used to indicate that there are global gaps between
    layers in the grid.

    With K gaps, the bottom of one layer need not be continuous with the
    top of the next layer, so the resulting number of intervals is
    greater than the number of layers.

    :ivar count: Number of gaps between layers. Must be positive. Number
        of INTERVALS = gapCount + NK.
    :ivar gap_after_layer: Boolean array of length NK-1. TRUE if there
        is a gap after the corresponding layer. NKL = NK + gapCount + 1
        BUSINESS RULE: gapCount must be consistent with the number of
        gaps specified by the gapAfterLayer array.
    """
    class Meta:
        name = "KGaps"

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    gap_after_layer: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "GapAfterLayer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
