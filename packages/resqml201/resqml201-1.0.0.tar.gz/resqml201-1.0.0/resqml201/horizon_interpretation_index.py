from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HorizonInterpretationIndex:
    """Element that lets you index and order horizon interpretations.

    For possible ordering criteria, see OrderingCriteria.

    :ivar index: An index value associated to an instance of this type
        of interpretation, given a specific ordering criteria
    :ivar stratigraphic_rank: Number of the stratigraphic rank on which
        the previous indices have been defined.
    :ivar horizon:
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    stratigraphic_rank: Optional[int] = field(
        default=None,
        metadata={
            "name": "StratigraphicRank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    horizon: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Horizon",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
