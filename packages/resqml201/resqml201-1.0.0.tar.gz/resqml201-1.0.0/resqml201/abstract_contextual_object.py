from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractContextualObject(AbstractObject):
    """
    Substitution group for contextual objects.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"
