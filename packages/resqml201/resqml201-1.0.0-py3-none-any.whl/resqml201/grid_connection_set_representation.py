from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_grid_connection_set_representation import ObjGridConnectionSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GridConnectionSetRepresentation(ObjGridConnectionSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
