from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.identity_kind import IdentityKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactIdentity:
    """Indicates identity between two (or more) contacts.

    For possible types of identities, see IdentityKind.

    :ivar identity_kind:
    :ivar list_of_contact_representations: The contact representations
        that share common identity as specified by their indices
    :ivar list_of_identical_nodes: Indicates which nodes (identified by
        their common index in all contact representations) of the
        contact representations are identical. If this list is not
        present, then it indicates that all nodes in each representation
        are identical, on an element by element level.
    """
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    list_of_contact_representations: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ListOfContactRepresentations",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    list_of_identical_nodes: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ListOfIdenticalNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
