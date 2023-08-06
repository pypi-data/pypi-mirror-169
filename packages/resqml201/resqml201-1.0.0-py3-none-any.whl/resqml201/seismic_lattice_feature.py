from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_seismic_lattice_feature import ObjSeismicLatticeFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLatticeFeature(ObjSeismicLatticeFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
