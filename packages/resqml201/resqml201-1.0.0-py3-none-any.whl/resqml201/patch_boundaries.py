from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PatchBoundaries:
    """Defines the boundaries of an indexed patch.

    These boundaries are outer and inner rings.

    :ivar inner_ring: A hole inside a representation patch. Inside the
        ring, the representation patch is not defined, outside it is. In
        case of contact, inner ring polyline representations should be
        typed as an erosion line, deposition line, or contact. BUSINESS
        RULE: Must be a polyline reference to a polyline representation,
        either a single polyline representation or a subrepresentation.
        Must be closed.
    :ivar outer_ring: The extension of a representation patch. Inside
        the ring, the representation patch is defined, outside it is
        not. BUSINESS RULE: Must be a reference to a polyline, either a
        single polyline representation or a subrepresentation. Must be
        closed.
    :ivar referenced_patch: UUID of the referenced topological patch.
    """
    inner_ring: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "InnerRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    outer_ring: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OuterRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    referenced_patch: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencedPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
