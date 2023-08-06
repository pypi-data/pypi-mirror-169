from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_property_kind import AbstractPropertyKind
from resqml201.resqml_property_kind import ResqmlPropertyKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StandardPropertyKind(AbstractPropertyKind):
    """A standard property kind is defined in the Energistics catalog.

    It has an unique name.
    """
    kind: Optional[ResqmlPropertyKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
