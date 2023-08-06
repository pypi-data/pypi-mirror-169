from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_parameter_key import AbstractParameterKey

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractActivityParameter:
    """
    General parameter value used in one instance of activity.

    :ivar title: Name of the parameter, used to identify it in the
        activity. Must have an equivalent in the activity descriptor
        parameters.
    :ivar index: When parameter is an array, used to indicate the index
        in the array
    :ivar selection: Textual description about how this parameter was
        selected.
    :ivar key:
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    selection: Optional[str] = field(
        default=None,
        metadata={
            "name": "Selection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    key: List[AbstractParameterKey] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
