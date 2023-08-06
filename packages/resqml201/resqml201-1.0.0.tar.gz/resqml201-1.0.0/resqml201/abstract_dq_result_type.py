from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_object_type import AbstractObjectType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqResultType(AbstractObjectType):
    class Meta:
        name = "AbstractDQ_Result_Type"
