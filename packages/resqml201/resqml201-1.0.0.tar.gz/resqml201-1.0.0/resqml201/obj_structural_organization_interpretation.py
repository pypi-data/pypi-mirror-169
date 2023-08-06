from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml201.data_object_reference import DataObjectReference
from resqml201.horizon_interpretation_index import HorizonInterpretationIndex
from resqml201.ordering_criteria import OrderingCriteria

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStructuralOrganizationInterpretation(AbstractOrganizationInterpretation):
    """
    One of the main types of RESQML organizations, this class gathers boundary
    interpretations (e.g., horizons and faults) plus frontier features and
    their relationships (contacts interpretations), which when taken together
    define the structure of a part of the earth.
    """
    class Meta:
        name = "obj_StructuralOrganizationInterpretation"

    ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "OrderingCriteria",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    faults: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Faults",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    horizons: List[HorizonInterpretationIndex] = field(
        default_factory=list,
        metadata={
            "name": "Horizons",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    sides: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Sides",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    top_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "TopFrontier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    bottom_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BottomFrontier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
