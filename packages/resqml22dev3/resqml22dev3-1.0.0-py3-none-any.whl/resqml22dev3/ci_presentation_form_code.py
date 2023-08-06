from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiPresentationFormCode(CodeListValueType):
    class Meta:
        name = "CI_PresentationFormCode"
        namespace = "http://www.isotc211.org/2005/gmd"
