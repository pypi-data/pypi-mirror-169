from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_parametric_line_array import AbstractParametricLineArray
from resqml201.data_object_reference import DataObjectReference
from resqml201.integer_lattice_array import IntegerLatticeArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineFromRepresentationLatticeArray(AbstractParametricLineArray):
    """The lattice array of parametric lines extracted from an existing
    representation.

    BUSINESS RULE: The supporting representation must have pillars or
    lines as indexable elements.

    :ivar line_indices_on_supporting_representation: The line indices of
        the selected lines in the supporting representation. The index
        selection is regularly incremented from one node to the next
        node. BUSINESS RULE: The dimensions of the integer lattice array
        must be consistent with the dimensions of the supporting
        representation. For a column-layer grid, the parametric lines
        follow the indexing of the pillars. BUSINESS RULE: The start
        value of the integer lattice array must be the linearized index
        of the starting line. Example: iStart + ni * jStart in case of a
        supporting 2D grid.
    :ivar supporting_representation:
    """
    line_indices_on_supporting_representation: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "LineIndicesOnSupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
