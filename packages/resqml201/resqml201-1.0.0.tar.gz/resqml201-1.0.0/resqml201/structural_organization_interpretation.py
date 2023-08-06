from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_structural_organization_interpretation import ObjStructuralOrganizationInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StructuralOrganizationInterpretation(ObjStructuralOrganizationInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
