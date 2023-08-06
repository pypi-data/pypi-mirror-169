from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_truncated_column_layer_grid_representation import AbstractTruncatedColumnLayerGridRepresentation
from resqml201.ijk_grid_geometry import IjkGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjTruncatedIjkGridRepresentation(AbstractTruncatedColumnLayerGridRepresentation):
    """Grid class with an underlying IJK topology, together with a 1D split
    cell list.

    The truncated IJK cells have more than the usual 6 faces. The split
    cells are arbitrary polyhedra, identical to those of an unstructured
    cell grid.

    :ivar ni: Count of I-indices in the grid. Must be positive.
    :ivar nj: Count of J-indices in the grid. Must be positive.
    :ivar geometry:
    """
    class Meta:
        name = "obj_TruncatedIjkGridRepresentation"

    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
