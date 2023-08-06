from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_parametric_line_geometry import AbstractParametricLineGeometry
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineFromRepresentationGeometry(AbstractParametricLineGeometry):
    """The parametric line extracted from an existing representation.

    BUSINESS RULE: The supporting representation must have pillars or
    lines as indexable elements.

    :ivar line_indiex_on_supporting_representation: The line index of
        the selected line in the supporting representation. For a
        column-layer grid, the parametric lines follow the indexing of
        the pillars.
    :ivar supporting_representation:
    """
    line_indiex_on_supporting_representation: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineIndiexOnSupportingRepresentation",
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
