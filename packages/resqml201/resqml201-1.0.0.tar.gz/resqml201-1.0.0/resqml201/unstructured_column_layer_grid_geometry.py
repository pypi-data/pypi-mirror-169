from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray
from resqml201.abstract_column_layer_grid_geometry import AbstractColumnLayerGridGeometry
from resqml201.column_shape import ColumnShape
from resqml201.resqml_jagged_array import ResqmlJaggedArray
from resqml201.unstructured_column_edges import UnstructuredColumnEdges

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredColumnLayerGridGeometry(AbstractColumnLayerGridGeometry):
    """Description of the geometry of an unstructured column layer grid, e.g.,
    parity and pinch, together with its supporting topology.

    Unstructured column layer cell geometry is derived from column layer
    cell geometry and hence is based upon nodes on coordinate lines.
    Geometry is contained within the representation of a grid.

    :ivar column_shape:
    :ivar pillar_count: Number of pillars in the grid. Must be positive.
        Pillars are used to describe the shape of the columns in the
        grid.
    :ivar pillars_per_column: List of pillars for each column. The
        pillars define the corners of each column. The number of pillars
        per column can be obtained from the offsets in the first list of
        list array. BUSINESS RULE: The length of the first array in the
        list of list construction should equal the columnCount.
    :ivar column_is_right_handed: List of columns which are right
        handed. Right handedness is evaluated following the pillar order
        and the K-direction tangent vector for each column.
    :ivar column_edges:
    """
    column_shape: Optional[ColumnShape] = field(
        default=None,
        metadata={
            "name": "ColumnShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillar_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PillarCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillars_per_column: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerColumn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    column_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "ColumnIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    column_edges: Optional[UnstructuredColumnEdges] = field(
        default=None,
        metadata={
            "name": "ColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
