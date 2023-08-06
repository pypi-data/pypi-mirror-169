from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.volume_uom import VolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class OverlapVolume:
    """Optional parent-child cell overlap volume information.

    If not present, then the CellOverlap data-object lists the overlaps,
    but with no additional information.

    :ivar volume_uom: Units of measure for the overlapVolume.
    :ivar overlap_volumes: Parent-child cell volume overlap. BUSINESS
        RULE: Length of array must equal the cell overlap count.
    """
    volume_uom: Optional[VolumeUom] = field(
        default=None,
        metadata={
            "name": "VolumeUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    overlap_volumes: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "OverlapVolumes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
