from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_double_table_lookup import ObjDoubleTableLookup

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DoubleTableLookup(ObjDoubleTableLookup):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
