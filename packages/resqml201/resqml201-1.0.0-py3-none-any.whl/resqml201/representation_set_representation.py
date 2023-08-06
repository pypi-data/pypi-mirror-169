from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_representation_set_representation import ObjRepresentationSetRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RepresentationSetRepresentation(ObjRepresentationSetRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
