from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.representation_identity import RepresentationIdentity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjRepresentationIdentitySet(AbstractResqmlDataObject):
    """
    A collection of representation identities.
    """
    class Meta:
        name = "obj_RepresentationIdentitySet"

    representation_identity: List[RepresentationIdentity] = field(
        default_factory=list,
        metadata={
            "name": "RepresentationIdentity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
