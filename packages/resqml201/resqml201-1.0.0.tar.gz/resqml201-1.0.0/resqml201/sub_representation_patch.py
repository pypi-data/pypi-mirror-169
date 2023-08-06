from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.element_indices import ElementIndices
from resqml201.patch1d import Patch1D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubRepresentationPatch(Patch1D):
    """Each sub-representation patch has its own list of representation
    indices, drawn from the supporting representation.

    If a list of pairwise elements is required, use two representation
    indices. The count of elements is defined in SubRepresenationPatch.
    Optional additional grid topology is available for grid
    representations.
    """
    element_indices: List[ElementIndices] = field(
        default_factory=list,
        metadata={
            "name": "ElementIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
