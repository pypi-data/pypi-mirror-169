from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml201.geologic_unit_composition import GeologicUnitComposition
from resqml201.geologic_unit_material_implacement import GeologicUnitMaterialImplacement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeologicUnitInterpretation(AbstractFeatureInterpretation):
    """
    The main class for data describing an opinion of a volume-based geologic
    feature or unit.
    """
    class Meta:
        name = "obj_GeologicUnitInterpretation"

    geologic_unit_composition: Optional[GeologicUnitComposition] = field(
        default=None,
        metadata={
            "name": "GeologicUnitComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geologic_unit_material_implacement: Optional[GeologicUnitMaterialImplacement] = field(
        default=None,
        metadata={
            "name": "GeologicUnitMaterialImplacement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
