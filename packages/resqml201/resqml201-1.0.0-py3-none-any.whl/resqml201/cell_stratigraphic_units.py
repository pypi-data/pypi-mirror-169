from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CellStratigraphicUnits:
    """
    A mapping from cell to stratigraphic unit interpretation for a
    representations (grids or blocked wells).

    :ivar unit_indices: Index of the stratigraphic unit of a given
        stratigraphic column for each cell. Use null (-1) if no
        stratigraphic column, e.g., within salt BUSINESS RULE: Array
        length is the number of cells in the grid or the blocked well
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
