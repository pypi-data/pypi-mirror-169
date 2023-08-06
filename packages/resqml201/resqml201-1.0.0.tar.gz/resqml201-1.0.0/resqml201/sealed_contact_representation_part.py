from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_contact_representation_part import AbstractContactRepresentationPart
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.contact_patch import ContactPatch
from resqml201.identity_kind import IdentityKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedContactRepresentationPart(AbstractContactRepresentationPart):
    """Sealed contact elements that indicate that 2 or more contact patches are
    partially or totally colocated or equivalent.

    For possible types of identity, see IdentityKind.

    :ivar identical_node_indices: Indicate which nodes (identified by
        their common index in all contact patches) of the contact
        patches are identical. If this list is not present, then it
        indicates that all nodes in each representation are identical,
        on an element-by-element level.
    :ivar identity_kind:
    :ivar contact:
    """
    identical_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IdenticalNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    contact: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
