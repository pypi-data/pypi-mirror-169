from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_global_chronostratigraphic_column import ObjGlobalChronostratigraphicColumn

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GlobalChronostratigraphicColumn(ObjGlobalChronostratigraphicColumn):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
