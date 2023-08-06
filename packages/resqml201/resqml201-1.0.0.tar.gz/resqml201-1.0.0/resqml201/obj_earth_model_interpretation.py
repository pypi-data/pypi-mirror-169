from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjEarthModelInterpretation(AbstractFeatureInterpretation):
    """An earth model interpretation has a specific role: it gathers a maximum
    of one of each of these other organization interpretations: structural
    organization interpretation, stratigraphic organization interpretation,
    and/or fluid organization interpretation.

    BUSINESS RULE: An earth model Interpretation interprets only an
    earth model feature.
    """
    class Meta:
        name = "obj_EarthModelInterpretation"

    stratigraphic_occurrences: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicOccurrences",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    stratigraphic_column: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "StratigraphicColumn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    structure: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    fluid: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Fluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
