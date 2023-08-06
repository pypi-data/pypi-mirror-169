from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineIntersections:
    """Used to specify the intersections between parametric lines.

    This information is purely geometric and is not required for the
    evaluation of the parametric point locations on these lines. The
    information required for that purpose is stored in the parametric
    points array.

    :ivar count: Number of parametric line intersections. Must be
        positive.
    :ivar intersection_line_pairs: Intersected line index pair for (line
        1, line 2). Size = 2 x count
    :ivar parameter_value_pairs: Intersected line parameter value pairs
        for (line 1, line 2). Size = 2 x count
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    intersection_line_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IntersectionLinePairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parameter_value_pairs: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "ParameterValuePairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
