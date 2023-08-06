from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_seismic_line_feature import ObjSeismicLineFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLineFeature(ObjSeismicLineFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
