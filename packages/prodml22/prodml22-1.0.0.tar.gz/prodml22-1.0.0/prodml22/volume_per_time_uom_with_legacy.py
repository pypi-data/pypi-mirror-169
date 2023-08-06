from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimeUomWithLegacy(Enum):
    """
    :cvar VALUE_1000SCF_D:
    :cvar VALUE_1000SCF_MO:
    :cvar VALUE_1000SCM_D:
    :cvar VALUE_1000SCM_MO:
    :cvar VALUE_1000STB_D:
    :cvar VALUE_1000STB_MO:
    :cvar VALUE_1_E6SCF_D:
    :cvar VALUE_1_E6SCF_MO:
    :cvar VALUE_1_E6SCM_D:
    :cvar VALUE_1_E6SCM_MO:
    :cvar VALUE_1_E6STB_D:
    :cvar VALUE_1_E6STB_MO:
    :cvar SCF_D:
    :cvar SCM_D:
    :cvar SCM_H:
    :cvar SCM_MO:
    :cvar SCM_S:
    :cvar STB_D:
    :cvar STB_MO:
    :cvar VALUE_1_30_CM3_MIN: cubic centimetre per thirty minute
    :cvar VALUE_1000_BBL_D: thousand barrel per day
    :cvar VALUE_1000_FT3_D: thousand cubic foot per day
    :cvar VALUE_1000_M3_D: thousand cubic metre per day
    :cvar VALUE_1000_M3_H: thousand cubic metre per hour
    :cvar VALUE_1_E6_BBL_D: million barrel per day
    :cvar VALUE_1_E6_FT3_D: million cubic foot per day
    :cvar VALUE_1_E6_M3_D: million cubic metre per day
    :cvar BBL_D: barrel per day
    :cvar BBL_H: barrel per hour
    :cvar BBL_MIN: barrel per minute
    :cvar CM3_H: cubic centimetre per hour
    :cvar CM3_MIN: cubic centimetre per minute
    :cvar CM3_S: cubic centimetre per second
    :cvar DM3_S: cubic decimetre per second
    :cvar FT3_D: cubic foot per day
    :cvar FT3_H: cubic foot per hour
    :cvar FT3_MIN: cubic foot per minute
    :cvar FT3_S: cubic foot per second
    :cvar GAL_UK_D: UK gallon per day
    :cvar GAL_UK_H: UK gallon per hour
    :cvar GAL_UK_MIN: UK gallon per minute
    :cvar GAL_US_D: US gallon per day
    :cvar GAL_US_H: US gallon per hour
    :cvar GAL_US_MIN: US gallon per minute
    :cvar L_H: litre per hour
    :cvar L_MIN: litre per minute
    :cvar L_S: litre per second
    :cvar M3_D: cubic metre per day
    :cvar M3_H: cubic metre per hour
    :cvar M3_MIN: cubic metre per minute
    :cvar M3_S: cubic metre per second
    """
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
    VALUE_1_30_CM3_MIN = "1/30 cm3/min"
    VALUE_1000_BBL_D = "1000 bbl/d"
    VALUE_1000_FT3_D = "1000 ft3/d"
    VALUE_1000_M3_D = "1000 m3/d"
    VALUE_1000_M3_H = "1000 m3/h"
    VALUE_1_E6_BBL_D = "1E6 bbl/d"
    VALUE_1_E6_FT3_D = "1E6 ft3/d"
    VALUE_1_E6_M3_D = "1E6 m3/d"
    BBL_D = "bbl/d"
    BBL_H = "bbl/h"
    BBL_MIN = "bbl/min"
    CM3_H = "cm3/h"
    CM3_MIN = "cm3/min"
    CM3_S = "cm3/s"
    DM3_S = "dm3/s"
    FT3_D = "ft3/d"
    FT3_H = "ft3/h"
    FT3_MIN = "ft3/min"
    FT3_S = "ft3/s"
    GAL_UK_D = "gal[UK]/d"
    GAL_UK_H = "gal[UK]/h"
    GAL_UK_MIN = "gal[UK]/min"
    GAL_US_D = "gal[US]/d"
    GAL_US_H = "gal[US]/h"
    GAL_US_MIN = "gal[US]/min"
    L_H = "L/h"
    L_MIN = "L/min"
    L_S = "L/s"
    M3_D = "m3/d"
    M3_H = "m3/h"
    M3_MIN = "m3/min"
    M3_S = "m3/s"
