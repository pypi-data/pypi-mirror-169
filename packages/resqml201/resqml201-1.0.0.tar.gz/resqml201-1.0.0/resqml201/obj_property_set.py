from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.data_object_reference import DataObjectReference
from resqml201.time_set_kind import TimeSetKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjPropertySet(AbstractResqmlDataObject):
    """A set of properties collected together for a specific purpose.

    For example, a property set can be used to collect all the
    properties corresponding to the simulation output at a single time,
    or all the values of a single property type for all times.

    :ivar time_set_kind:
    :ivar has_single_property_kind: If true, indicates that the
        collection contains only property values associated with a
        single property kind.
    :ivar has_multiple_realizations: If true, indicates that the
        collection contains properties with defined realization indices.
    :ivar parent_set: A pointer to the parent property group of this
        property group.
    :ivar properties:
    """
    class Meta:
        name = "obj_PropertySet"

    time_set_kind: Optional[TimeSetKind] = field(
        default=None,
        metadata={
            "name": "TimeSetKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    has_single_property_kind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasSinglePropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    has_multiple_realizations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMultipleRealizations",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_set: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ParentSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    properties: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
