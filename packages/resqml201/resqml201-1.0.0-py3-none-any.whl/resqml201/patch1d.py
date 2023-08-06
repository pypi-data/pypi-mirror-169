from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.patch import Patch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Patch1D(Patch):
    """
    A patch with a single 1D index count.

    :ivar count: Number of items in the patch.
    """
    class Meta:
        name = "Patch1d"

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
