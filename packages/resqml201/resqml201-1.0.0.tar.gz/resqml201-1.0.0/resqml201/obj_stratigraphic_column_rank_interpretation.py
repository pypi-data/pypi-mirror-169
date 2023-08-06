from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_stratigraphic_organization_interpretation import AbstractStratigraphicOrganizationInterpretation
from resqml201.stratigraphic_unit_interpretation_index import StratigraphicUnitInterpretationIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStratigraphicColumnRankInterpretation(AbstractStratigraphicOrganizationInterpretation):
    """
    A global hierarchy containing an ordered list of stratigraphic unit
    interpretations.
    """
    class Meta:
        name = "obj_StratigraphicColumnRankInterpretation"

    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    stratigraphic_units: List[StratigraphicUnitInterpretationIndex] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
