from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.parameter_template import ParameterTemplate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjActivityTemplate(AbstractResqmlDataObject):
    """
    Description of one type of activity.
    """
    class Meta:
        name = "obj_ActivityTemplate"

    parameter: List[ParameterTemplate] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
