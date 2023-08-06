from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_streamlines_feature import ObjStreamlinesFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StreamlinesFeature(ObjStreamlinesFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
