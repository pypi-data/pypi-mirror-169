from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_tectonic_boundary_feature import ObjTectonicBoundaryFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TectonicBoundaryFeature(ObjTectonicBoundaryFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
