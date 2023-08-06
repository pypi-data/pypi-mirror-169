from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_grid_representation import AbstractGridRepresentation
from resqml201.gp_grid_column_layer_grid import GpGridColumnLayerGrid
from resqml201.gp_grid_unstructured_grid_patch import GpGridUnstructuredGridPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGpGridRepresentation(AbstractGridRepresentation):
    """General purpose (GP) grid representation, which includes and/or extends
    the features from all other grid representations.

    This general purpose representation is included in the schema for
    research and/or advanced modeling purposes, but is not expected to
    be used for routine data transfer.
    """
    class Meta:
        name = "obj_GpGridRepresentation"

    column_layer_grid: List[GpGridColumnLayerGrid] = field(
        default_factory=list,
        metadata={
            "name": "ColumnLayerGrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    unstructured_grid_patch: List[GpGridUnstructuredGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
