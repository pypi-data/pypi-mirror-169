from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjRepresentationSetRepresentation(AbstractRepresentation):
    """The parent class of the framework representations.

    It is used to group together individual representations which may be
    of the same kind to represent a "bag" of representations. If the bag
    is homogeneous, then this may be indicated. These "bags" do not
    imply any geologic consistency. For example, you can define a set of
    wellbore frames, a set of wellbore trajectories, a set of blocked
    wellbores. Because the framework representations inherit from this
    class, they inherit the capability to gather individual
    representations into sealed and non-sealed surface framework
    representations, or sealed volume framework representations.

    :ivar is_homogeneous: Indicates that all of the selected
        representations are of a single kind.
    :ivar representation:
    """
    class Meta:
        name = "obj_RepresentationSetRepresentation"

    is_homogeneous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsHomogeneous",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
