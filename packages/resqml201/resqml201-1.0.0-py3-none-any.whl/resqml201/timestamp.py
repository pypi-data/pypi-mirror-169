from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Timestamp:
    """
    Time.

    :ivar date_time: A date which can be represented according to the
        W3CDTF format.
    :ivar year_offset: Indicates that the dateTime attribute must be
        translated according to this value.
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    year_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "YearOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
