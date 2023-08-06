from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_geologic_unit_feature import ObjGeologicUnitFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeobodyFeature(ObjGeologicUnitFeature):
    """A volume of rock that is identified based on some specific attribute,
    like its mineral content or other physical characteristic.

    Unlike stratigraphic or phase units, there is no associated time or
    fluid content semantic. For types, see GeobodyKind.
    """
    class Meta:
        name = "obj_GeobodyFeature"
