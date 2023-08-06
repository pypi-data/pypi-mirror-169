from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml201.grid2d_patch import Grid2DPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGrid2DSetRepresentation(AbstractSurfaceRepresentation):
    """Set of representations based on a 2D grid.

    Each 2D grid representation corresponds to one patch of the set.
    """
    class Meta:
        name = "obj_Grid2dSetRepresentation"

    grid2d_patch: List[Grid2DPatch] = field(
        default_factory=list,
        metadata={
            "name": "Grid2dPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
