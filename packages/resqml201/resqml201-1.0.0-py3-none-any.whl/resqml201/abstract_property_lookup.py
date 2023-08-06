from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractPropertyLookup(AbstractResqmlDataObject):
    """Generic representation of a property lookup table.

    Each derived element provides specific lookup methods for different
    data types.
    """
