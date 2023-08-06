from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml201.grid2d_patch import Grid2DPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGrid2DRepresentation(AbstractSurfaceRepresentation):
    """Representation based on a 2D grid.

    For definitions of slowest and fastest axes of the array, see
    Grid2dPatch.
    """
    class Meta:
        name = "obj_Grid2dRepresentation"

    grid2d_patch: Optional[Grid2DPatch] = field(
        default=None,
        metadata={
            "name": "Grid2dPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
