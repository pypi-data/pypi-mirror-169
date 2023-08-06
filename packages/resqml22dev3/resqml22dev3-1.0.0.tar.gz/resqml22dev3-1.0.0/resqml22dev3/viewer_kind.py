from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ViewerKind(Enum):
    VALUE_3D = "3d"
    BASE_MAP = "base map"
    SECTION = "section"
    WELL_CORRELATION = "well correlation"
