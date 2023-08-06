from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.citation import Citation
from resqml201.custom_data import CustomData
from resqml201.object_alias import ObjectAlias

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractObject:
    """The intended abstract supertype of all schema roots that may be a member
    of a substitution group (whether contextual or data).

    The type of root global elements should be extended from this type
    and the root global element should be declared to be a member of one
    of the above substitution groups.

    :ivar citation:
    :ivar aliases:
    :ivar custom_data:
    :ivar schema_version: The specific version of a schema from which
        this object is derived. This string should be exactly equivalent
        to the version attribute of the root element of the associated
        XSD schema file. In the UML model is the same as the version
        tagged value of the &lt;&lt;XSDschema&gt;&gt; package.
    :ivar uuid:
    :ivar object_version:
    """
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
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
