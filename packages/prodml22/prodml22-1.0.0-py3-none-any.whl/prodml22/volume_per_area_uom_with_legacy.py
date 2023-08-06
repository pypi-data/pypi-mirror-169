from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerAreaUomWithLegacy(Enum):
    """
    :cvar VALUE_1_E6STB_ACRE:
    :cvar SCF_FT2:
    :cvar SCM_M2:
    :cvar STB_ACRE:
    :cvar VALUE_1_E6_BBL_ACRE: million barrel per acre
    :cvar BBL_ACRE: barrel per acre
    :cvar FT3_FT2: cubic foot per square foot
    :cvar M3_M2: cubic metre per square metre
    """
    VALUE_1_E6STB_ACRE = "1E6stb/acre"
    SCF_FT2 = "scf/ft2"
    SCM_M2 = "scm/m2"
    STB_ACRE = "stb/acre"
    VALUE_1_E6_BBL_ACRE = "1E6 bbl/acre"
    BBL_ACRE = "bbl/acre"
    FT3_FT2 = "ft3/ft2"
    M3_M2 = "m3/m2"
