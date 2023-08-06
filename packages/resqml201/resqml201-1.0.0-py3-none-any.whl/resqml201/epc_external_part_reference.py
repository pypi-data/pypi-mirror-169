from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_epc_external_part_reference import ObjEpcExternalPartReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EpcExternalPartReference(ObjEpcExternalPartReference):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"
