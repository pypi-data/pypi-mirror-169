from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_object_type import AbstractObjectType
from resqml201.character_string_property_type import CharacterStringPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiTelephoneType(AbstractObjectType):
    """
    Telephone numbers for contacting the responsible individual or
    organisation.
    """
    class Meta:
        name = "CI_Telephone_Type"

    voice: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    facsimile: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
