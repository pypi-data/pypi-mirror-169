from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_cited_data_object import AbstractCitedDataObject
from resqml201.name_value_pair import NameValuePair

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractResqmlDataObject(AbstractCitedDataObject):
    """The parent class for all top-level elements in RESQML.

    Inherits from AbstractCitedDataObject in the commonV2 package of the
    model.
    """
    extra_metadata: List[NameValuePair] = field(
        default_factory=list,
        metadata={
            "name": "ExtraMetadata",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
