from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_ijk_grid_representation import ObjIjkGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjkGridRepresentation(ObjIjkGridRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
