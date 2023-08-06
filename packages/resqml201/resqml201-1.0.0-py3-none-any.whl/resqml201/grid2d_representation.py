from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_grid2d_representation import ObjGrid2DRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DRepresentation(ObjGrid2DRepresentation):
    class Meta:
        name = "Grid2dRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
