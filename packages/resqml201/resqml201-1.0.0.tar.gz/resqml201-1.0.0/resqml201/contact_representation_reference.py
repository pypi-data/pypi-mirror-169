from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_contact_representation_part import AbstractContactRepresentationPart
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactRepresentationReference(AbstractContactRepresentationPart):
    """
    Used when the contact already exists as a top level element representation.
    """
    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
