from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_streamlines_representation import ObjStreamlinesRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StreamlinesRepresentation(ObjStreamlinesRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
