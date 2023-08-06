from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_technical_feature import AbstractTechnicalFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjFrontierFeature(AbstractTechnicalFeature):
    """
    Identifies a frontier or boundary in the earth model that is not a
    geological feature but an arbitrary geographic/geometric surface used to
    delineate the boundary of the model.
    """
    class Meta:
        name = "obj_FrontierFeature"
