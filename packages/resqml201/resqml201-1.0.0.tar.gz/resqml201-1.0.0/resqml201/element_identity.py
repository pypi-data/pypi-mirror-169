from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.data_object_reference import DataObjectReference
from resqml201.identity_kind import IdentityKind
from resqml201.indexable_elements import IndexableElements
from resqml201.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ElementIdentity:
    """Indicates the nature of the relationship between 2 or more
    representations, specifically if they are partially or totally identical.

    For possible types of relationships, see IdentityKind. Commonly used
    to identify contacts between representations in model descriptions.
    May also be used to relate the components of a grid (e.g., pillars)
    to those of a structural framework.

    :ivar element_indices: Indicates which elements are identical based
        on their indices in the (sub)representation. If not given, then
        the selected indexable elements of each of the selected
        representations are identical at the element by element level.
        If not given, then all elements are specified to be identical.
        BUSINESS RULE: Number of identical elements must equal
        identicalElementCount for each representation.
    :ivar identity_kind:
    :ivar indexable_element:
    :ivar representation:
    :ivar from_time_index:
    :ivar to_time_index:
    """
    element_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ElementIndices",
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
    indexable_element: Optional[IndexableElements] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    from_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "FromTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    to_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "ToTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
