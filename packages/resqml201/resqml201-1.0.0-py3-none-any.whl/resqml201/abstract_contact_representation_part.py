from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractContactRepresentationPart:
    """
    Parent class of the sealed and nonsealed contact elements.

    :ivar index: The index of the contact. Indicates identity of the
        contact in the surface framework context. It is used for contact
        identities and to find the interpretation of this particular
        contact.
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
