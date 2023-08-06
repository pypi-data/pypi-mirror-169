from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_representation_identity_set import ObjRepresentationIdentitySet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RepresentationIdentitySet(ObjRepresentationIdentitySet):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
