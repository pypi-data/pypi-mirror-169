from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.abstract_parent_window import AbstractParentWindow
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CellParentWindow(AbstractParentWindow):
    """
    Parent window for ANY grid indexed as if it were an unstructured cell grid,
    i.e., using a 1D index.

    :ivar cell_indices: Cell indices which list the cells in the parent
        window. BUSINESS RULE: Number of cells must be consistent with
        the child grid cell count.
    :ivar parent_grid:
    """
    cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_grid: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentGrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
