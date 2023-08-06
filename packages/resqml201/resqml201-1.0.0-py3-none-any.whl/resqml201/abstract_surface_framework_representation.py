from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.contact_identity import ContactIdentity
from resqml201.obj_representation_set_representation import ObjRepresentationSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractSurfaceFrameworkRepresentation(ObjRepresentationSetRepresentation):
    """Parent class for a sealed or non-sealed surface framework
    representation.

    Each one instantiates a representation set representation. The
    difference between the sealed and non-sealed frameworks is that, in
    the non-sealed case, we do not have all of the contact
    representations, or we have all of the contacts but they are not all
    sealed.
    """
    contact_identity: List[ContactIdentity] = field(
        default_factory=list,
        metadata={
            "name": "ContactIdentity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
