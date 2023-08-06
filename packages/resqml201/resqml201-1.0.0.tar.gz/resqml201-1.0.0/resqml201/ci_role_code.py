from __future__ import annotations
from dataclasses import dataclass
from resqml201.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiRoleCode(CodeListValueType):
    class Meta:
        name = "CI_RoleCode"
        namespace = "http://www.isotc211.org/2005/gmd"
