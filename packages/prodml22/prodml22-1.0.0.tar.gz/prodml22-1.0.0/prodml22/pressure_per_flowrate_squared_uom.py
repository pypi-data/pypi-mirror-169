from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressurePerFlowrateSquaredUom(Enum):
    BAR_1000M3_DAY_2 = "bar/(1000m3/day)2"
    BAR_M3_DAY_2 = "bar/(m3/day)2"
    PA_1000M3_DAY_2 = "Pa/(1000m3/day)2"
    PA_M3_DAY_2 = "Pa/(m3/day)2"
    PSI_1000000FT3_DAY_2 = "psi/(1000000ft3/day)2"
    PSI_1000FT3_DAY_2 = "psi/(1000ft3/day)2"
    PSI_BBL_DAY_2 = "psi/(bbl/day)2"
