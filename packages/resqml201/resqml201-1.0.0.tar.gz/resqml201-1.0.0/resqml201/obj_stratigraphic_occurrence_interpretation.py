from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_stratigraphic_organization_interpretation import AbstractStratigraphicOrganizationInterpretation
from resqml201.data_object_reference import DataObjectReference
from resqml201.geologic_unit_interpretation_index import GeologicUnitInterpretationIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStratigraphicOccurrenceInterpretation(AbstractStratigraphicOrganizationInterpretation):
    """A local Interpretation—it could be along a well, on a 2D map, or on a 2D
    section or on a part of the global volume of an earth model—of a succession
    of rock feature elements.

    The stratigraphic column rank interpretation composing a
    stratigraphic occurrence can be ordered by the criteria listed in
    OrderingCriteria. BUSINESS RULE: A representation of a stratigraphic
    occurrence interpretation can be a wellbore marker or a wellbore
    frame.
    """
    class Meta:
        name = "obj_StratigraphicOccurrenceInterpretation"

    is_occurrence_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsOccurrenceOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geologic_unit_index: List[GeologicUnitInterpretationIndex] = field(
        default_factory=list,
        metadata={
            "name": "GeologicUnitIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
