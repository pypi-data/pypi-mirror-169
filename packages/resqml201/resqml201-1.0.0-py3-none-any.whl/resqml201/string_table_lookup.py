from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_string_table_lookup import ObjStringTableLookup

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StringTableLookup(ObjStringTableLookup):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
