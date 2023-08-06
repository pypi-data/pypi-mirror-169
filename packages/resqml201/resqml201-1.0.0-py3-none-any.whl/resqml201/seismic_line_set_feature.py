from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_seismic_line_set_feature import ObjSeismicLineSetFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLineSetFeature(ObjSeismicLineSetFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
