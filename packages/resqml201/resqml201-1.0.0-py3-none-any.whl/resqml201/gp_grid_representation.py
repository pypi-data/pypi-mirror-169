from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_gp_grid_representation import ObjGpGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridRepresentation(ObjGpGridRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
