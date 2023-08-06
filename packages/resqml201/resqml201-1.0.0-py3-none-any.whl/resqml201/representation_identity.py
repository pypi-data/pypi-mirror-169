from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.additional_grid_topology import AdditionalGridTopology
from resqml201.element_identity import ElementIdentity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RepresentationIdentity:
    """Indicates the nature of the relationship between 2 or more
    representations, specifically if they are partially or totally identical.

    For possible types of relationships, see IdentityKind.

    :ivar identical_element_count: Number of elements within each
        representation for which a representation identity is specified.
    :ivar element_identity:
    :ivar additional_grid_topology:
    """
    identical_element_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IdenticalElementCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    element_identity: List[ElementIdentity] = field(
        default_factory=list,
        metadata={
            "name": "ElementIdentity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
    additional_grid_topology: Optional[AdditionalGridTopology] = field(
        default=None,
        metadata={
            "name": "AdditionalGridTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
