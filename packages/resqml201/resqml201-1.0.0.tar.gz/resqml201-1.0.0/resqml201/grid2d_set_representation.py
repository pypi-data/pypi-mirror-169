from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_grid2d_set_representation import ObjGrid2DSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DSetRepresentation(ObjGrid2DSetRepresentation):
    class Meta:
        name = "Grid2dSetRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
