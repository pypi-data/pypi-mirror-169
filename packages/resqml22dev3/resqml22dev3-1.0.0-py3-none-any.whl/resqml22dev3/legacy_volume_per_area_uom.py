from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyVolumePerAreaUom(Enum):
    VALUE_1_E6STB_ACRE = "1E6stb/acre"
    SCF_FT2 = "scf/ft2"
    SCM_M2 = "scm/m2"
    STB_ACRE = "stb/acre"
