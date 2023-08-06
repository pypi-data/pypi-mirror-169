from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_property_kind import AbstractPropertyKind
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalPropertyKind(AbstractPropertyKind):
    local_property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
