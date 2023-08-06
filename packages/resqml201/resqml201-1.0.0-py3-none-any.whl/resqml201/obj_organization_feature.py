from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_geologic_feature import AbstractGeologicFeature
from resqml201.organization_kind import OrganizationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjOrganizationFeature(AbstractGeologicFeature):
    """The explicit description of the relationships between geologic features,
    such as rock features (e.g., stratigraphic units, geobodies, phase unit)
    and boundary features (e.g., genetic, tectonic, and fluid boundaries).

    For types of organizations, see OrganizationKind.
    """
    class Meta:
        name = "obj_OrganizationFeature"

    organization_kind: Optional[OrganizationKind] = field(
        default=None,
        metadata={
            "name": "OrganizationKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
