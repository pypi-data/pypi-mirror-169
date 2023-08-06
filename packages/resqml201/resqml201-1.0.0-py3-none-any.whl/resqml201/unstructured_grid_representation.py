from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_unstructured_grid_representation import ObjUnstructuredGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredGridRepresentation(ObjUnstructuredGridRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
