from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_geologic_feature import AbstractGeologicFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeologicUnitFeature(AbstractGeologicFeature):
    """A volume of rock located between one or more boundary features.

    The limiting boundary features should be genetic boundary features
    (i.e. should not be faults).
    """
    class Meta:
        name = "obj_GeologicUnitFeature"
