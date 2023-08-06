from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IntervalStratigraphicUnits:
    """
    A mapping from intervals to stratigraphic units for representations (grids
    or wellbore frames).

    :ivar unit_indices: Index of the stratigraphic unit per interval, of
        a given stratigraphic column. Notes: 1.) For grids, intervals =
        layers + K gaps. 2.) If there is no stratigraphic column, e.g.,
        within salt, use null (-1) BUSINESS RULE: Array length must
        equal the number of INTERVALS.
    :ivar stratigraphic_organization:
    """
    unit_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "UnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    stratigraphic_organization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "StratigraphicOrganization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
