from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PropertyValuesPatch:
    patch_uid: Optional[int] = field(
        default=None,
        metadata={
            "name": "patchUid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    values: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
