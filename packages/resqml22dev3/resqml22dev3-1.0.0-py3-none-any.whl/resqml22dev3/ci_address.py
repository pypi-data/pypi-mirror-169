from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.ci_address_type import CiAddressType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiAddress(CiAddressType):
    class Meta:
        name = "CI_Address"
        namespace = "http://www.isotc211.org/2005/gmd"
