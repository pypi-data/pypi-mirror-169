from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.resqml_jagged_array import ResqmlJaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjSplitColumnEdges:
    """Used to construct the indices for the cell faces.

    For IJK grids with IJ gaps, the split column edge indices must be
    defined explicitly. Otherwise, column edges are not required to
    describe the lowest order grid geometry, but may be needed for
    higher order geometries or properties.

    :ivar count: Number of IJ split column edges in this grid. Must be
        positive.
    :ivar pillars_per_split_column_edge: Definition of the split column
        edges in terms of the pillars per split column edge. Pillar
        count per edge is usually 2, but the list-of-lists construction
        is used to allow split column edges to be defined by more than 2
        pillars.
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillars_per_split_column_edge: Optional[ResqmlJaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerSplitColumnEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
