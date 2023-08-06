from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.chronostratigraphic_rank import ChronostratigraphicRank

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGlobalChronostratigraphicColumn(AbstractResqmlDataObject):
    """
    Chronological successions of some chronostratigraphic units organized into
    1 to n chronological ranks.
    """
    class Meta:
        name = "obj_GlobalChronostratigraphicColumn"

    chronostratigraphic_column_component: List[ChronostratigraphicRank] = field(
        default_factory=list,
        metadata={
            "name": "ChronostratigraphicColumnComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
