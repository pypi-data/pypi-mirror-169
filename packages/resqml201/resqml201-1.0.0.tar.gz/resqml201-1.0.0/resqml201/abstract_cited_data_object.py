from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.citation import Citation
from resqml201.custom_data import CustomData
from resqml201.object_alias import ObjectAlias

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractCitedDataObject:
    """The Mother Class for all Top Level Elements in RESQML.

    Inherits from the commonv2 AbstractDataObject. The purpose of this
    derivation is simply to make the Citation element mandatory.
    Appropriate to use as a base class in any ML where this is desired.
    """
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    aliases: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "Aliases",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    custom_data: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "CustomData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectVersion",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
            "white_space": "collapse",
        }
    )
