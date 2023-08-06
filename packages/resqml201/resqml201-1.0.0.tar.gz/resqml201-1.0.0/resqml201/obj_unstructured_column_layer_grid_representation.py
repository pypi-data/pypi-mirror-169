from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_column_layer_grid_representation import AbstractColumnLayerGridRepresentation
from resqml201.unstructured_column_layer_grid_geometry import UnstructuredColumnLayerGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjUnstructuredColumnLayerGridRepresentation(AbstractColumnLayerGridRepresentation):
    """Grid whose topology is characterized by an unstructured column index and
    a layer index, K.

    Cell geometry is characterized by nodes on coordinate lines, where
    each column of the model may have an arbitrary number of sides.

    :ivar column_count: Number of unstructured columns in the grid. Must
        be positive.
    :ivar geometry:
    """
    class Meta:
        name = "obj_UnstructuredColumnLayerGridRepresentation"

    column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ColumnCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
