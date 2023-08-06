from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyVolumePerVolumeUom(Enum):
    VALUE_1000SCF_STB = "1000scf/stb"
    VALUE_1_E6SCF_STB = "1E6scf/stb"
    VALUE_1_E6STB_ACRE_FT = "1E6stb/acre.ft"
    ACRE_FT_1_E6STB = "acre.ft/1E6stb"
    BBL_1000SCF = "bbl/1000scf"
    BBL_1_E6SCF = "bbl/1E6scf"
    BBL_SCF = "bbl/scf"
    BBL_STB = "bbl/stb"
    FT3_SCF = "ft3/scf"
    FT3_STB = "ft3/stb"
    GAL_US_1000SCF = "galUS/1000scf"
    M3_SCM = "m3/scm"
    ML_SCM = "ml/scm"
    SCF_BBL = "scf/bbl"
    SCF_FT3 = "scf/ft3"
    SCF_SCF = "scf/scf"
    SCF_STB = "scf/stb"
    SCM_M3 = "scm/m3"
    SCM_SCM = "scm/scm"
    SCM_STB = "scm/stb"
    STB_1000SCF = "stb/1000scf"
    STB_1000SCM = "stb/1000scm"
    STB_1_E6SCF = "stb/1E6scf"
    STB_1_E6SCM = "stb/1E6scm"
    STB_BBL = "stb/bbl"
    STB_SCM = "stb/scm"
    STB_STB = "stb/stb"
