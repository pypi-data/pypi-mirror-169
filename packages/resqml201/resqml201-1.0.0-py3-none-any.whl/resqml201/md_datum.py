from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_md_datum import ObjMdDatum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MdDatum(ObjMdDatum):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
