from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyVolumePerTimeUom(Enum):
    VALUE_1000SCF_D = "1000scf/d"
    VALUE_1000SCF_MO = "1000scf/mo"
    VALUE_1000SCM_D = "1000scm/d"
    VALUE_1000SCM_MO = "1000scm/mo"
    VALUE_1000STB_D = "1000stb/d"
    VALUE_1000STB_MO = "1000stb/mo"
    VALUE_1_E6SCF_D = "1E6scf/d"
    VALUE_1_E6SCF_MO = "1E6scf/mo"
    VALUE_1_E6SCM_D = "1E6scm/d"
    VALUE_1_E6SCM_MO = "1E6scm/mo"
    VALUE_1_E6STB_D = "1E6stb/d"
    VALUE_1_E6STB_MO = "1E6stb/mo"
    SCF_D = "scf/d"
    SCM_D = "scm/d"
    SCM_H = "scm/h"
    SCM_MO = "scm/mo"
    SCM_S = "scm/s"
    STB_D = "stb/d"
    STB_MO = "stb/mo"
