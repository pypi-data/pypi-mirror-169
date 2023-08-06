from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_truncated_unstructured_column_layer_grid_representation import ObjTruncatedUnstructuredColumnLayerGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TruncatedUnstructuredColumnLayerGridRepresentation(ObjTruncatedUnstructuredColumnLayerGridRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
