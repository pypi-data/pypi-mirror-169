from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.facet import Facet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PropertyKindFacet:
    """Qualifiers for property values, which allows users to semantically
    specialize a property without creating a new property kind.

    For the list of enumerations, see Facet.

    :ivar facet: Facet of the property kind (see the enumeration)
    :ivar value: Property facet value.
    """
    facet: Optional[Facet] = field(
        default=None,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
