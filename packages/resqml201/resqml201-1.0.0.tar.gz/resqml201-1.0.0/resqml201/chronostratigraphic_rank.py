from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ChronostratigraphicRank:
    """The chronostratigraphic ranking of "well known" stratigraphic unit
    features in the global chronostratigraphic column.

    The ranks are organized from container to contained, e.g., (eon=1),
    (era=2), (period=3) The units are ranked by using age as ordering
    criteria, from oldest to youngest. These stratigraphic units have no
    associated interpretations or representations. BUSINESS RULE: The
    name must reference a well-known stratigraphic unit feature (such as
    "Jurassic"), for example, from the International Commission on
    Stratigraphy (http://www.stratigraphy.org).

    :ivar name: Name of the chrono rank such as "epoch, era, ..."
    :ivar contains:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_length": 1,
            "max_length": 64,
            "white_space": "collapse",
        }
    )
    contains: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
