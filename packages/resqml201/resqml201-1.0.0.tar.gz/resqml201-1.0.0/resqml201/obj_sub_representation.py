from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.additional_grid_topology import AdditionalGridTopology
from resqml201.data_object_reference import DataObjectReference
from resqml201.sub_representation_patch import SubRepresentationPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjSubRepresentation(AbstractRepresentation):
    """An ordered list of indexable elements and/or indexable element pairs of
    an existing representation.

    Because the representation concepts of topology, geometry, and
    property values are separate in RESQML, it is now possible to select
    a range of nodes, edges, faces, or volumes (cell) indices from the
    topological support of an existing representation to define a sub-
    representation. A sub-representation may describe a different
    feature interpretation using the same geometry or property as the
    "parent" representation. In this case, the only information
    exchanged is a set of potentially non-consecutive indices of the
    topological support of the representation.
    """
    class Meta:
        name = "obj_SubRepresentation"

    additional_grid_topology: Optional[AdditionalGridTopology] = field(
        default=None,
        metadata={
            "name": "AdditionalGridTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    sub_representation_patch: List[SubRepresentationPatch] = field(
        default_factory=list,
        metadata={
            "name": "SubRepresentationPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
