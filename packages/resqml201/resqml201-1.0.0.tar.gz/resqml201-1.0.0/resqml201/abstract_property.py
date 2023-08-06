from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_property_kind import AbstractPropertyKind
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.data_object_reference import DataObjectReference
from resqml201.indexable_elements import IndexableElements
from resqml201.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractProperty(AbstractResqmlDataObject):
    """Base class for storing all property values on representations, except
    current geometry location.

    Values attached to a given element can be either a scalar or a
    vector. The size of the vector is constant on all elements, and it
    is assumed that all elements of the vector have identical property
    types and share the same unit of measure.

    :ivar count: Number of elements in a 1D list of properties. When
        used in a multi-dimensional array, count is always the fastest.
    :ivar indexable_element:
    :ivar realization_index: Optional element indicating the realization
        index (metadata). Used if the property is the result of a multi-
        realization process.
    :ivar time_step: Indicates that the property is the output of a
        specific time step from a flow simulator. Time step is metadata
        that makes sense in the context of a specific simulation run,
        and should not be confused with the time index.
    :ivar time_index:
    :ivar supporting_representation:
    :ivar local_crs:
    :ivar property_kind:
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
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
    realization_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RealizationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    time_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeStep",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    property_kind: Optional[AbstractPropertyKind] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
