from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.contact_mode import ContactMode
from resqml201.contact_side import ContactSide
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactElementReference(DataObjectReference):
    """A reference to either a geologic feature interpretation or a frontier
    feature.

    BUSINESS RULE: The ContentType of the corresponding data-object
    reference must be a geological feature interpretation or a frontier
    feature.
    """
    qualifier: Optional[ContactSide] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    secondary_qualifier: Optional[ContactMode] = field(
        default=None,
        metadata={
            "name": "SecondaryQualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
