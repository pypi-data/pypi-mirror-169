from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_truncated_ijk_grid_representation import ObjTruncatedIjkGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TruncatedIjkGridRepresentation(ObjTruncatedIjkGridRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
