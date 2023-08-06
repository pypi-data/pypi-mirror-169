from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStratigraphicColumn(AbstractResqmlDataObject):
    """A global interpretation of the stratigraphy, which can be made up of
    several ranks of stratigraphic unit interpretations.

    BUSINESS RULE: All stratigraphic column rank interpretations that
    make up a stratigraphic column must be ordered by age.
    """
    class Meta:
        name = "obj_StratigraphicColumn"

    ranks: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Ranks",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
