from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_stratigraphic_column_rank_interpretation import ObjStratigraphicColumnRankInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicColumnRankInterpretation(ObjStratigraphicColumnRankInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
