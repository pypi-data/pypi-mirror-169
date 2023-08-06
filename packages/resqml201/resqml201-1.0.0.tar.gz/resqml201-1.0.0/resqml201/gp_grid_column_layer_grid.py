from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.gp_grid_ijk_grid_patch import GpGridIjkGridPatch
from resqml201.gp_grid_unstructured_column_layer_grid_patch import GpGridUnstructuredColumnLayerGridPatch
from resqml201.kgaps import Kgaps

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridColumnLayerGrid:
    """Used to construct a column layer grid patch based upon multiple
    unstructured column layer and IJK grids which share a layering scheme.

    Multiple patches are supported.

    :ivar nk: Number of layers. Degenerate case (nk=0) is allowed for
        GPGrid.
    :ivar kgaps:
    :ivar ijk_grid_patch:
    :ivar unstructured_column_layer_grid_patch:
    """
    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    kgaps: Optional[Kgaps] = field(
        default=None,
        metadata={
            "name": "KGaps",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    ijk_grid_patch: List[GpGridIjkGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "IjkGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    unstructured_column_layer_grid_patch: List[GpGridUnstructuredColumnLayerGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredColumnLayerGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
