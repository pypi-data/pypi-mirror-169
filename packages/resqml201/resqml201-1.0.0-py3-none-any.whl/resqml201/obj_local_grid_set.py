from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.activation import Activation
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjLocalGridSet(AbstractResqmlDataObject):
    """Used to activate and/or deactivate the specified children grids as local
    grids on their parents.

    Once activated, this object indicates that a child grid replaces
    local portions of the corresponding parent grid. Parentage is
    inferred from the child grid construction. Without a grid set
    activation, the local grids are always active. Otherwise, the grid
    set activation is used to activate and/or deactivate the local grids
    in the set at specific times.
    """
    class Meta:
        name = "obj_LocalGridSet"

    activation: Optional[Activation] = field(
        default=None,
        metadata={
            "name": "Activation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    child_grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ChildGrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
