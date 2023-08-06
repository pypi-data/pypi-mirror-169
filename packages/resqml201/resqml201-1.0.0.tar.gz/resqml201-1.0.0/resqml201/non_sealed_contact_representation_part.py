from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_contact_representation_part import AbstractContactRepresentationPart
from resqml201.abstract_geometry import AbstractGeometry
from resqml201.contact_patch import ContactPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NonSealedContactRepresentationPart(AbstractContactRepresentationPart):
    """
    Defines a nonsealed contact representation, meaning that this contact
    representation is defined by a geometry.
    """
    contact: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geometry: Optional[AbstractGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
