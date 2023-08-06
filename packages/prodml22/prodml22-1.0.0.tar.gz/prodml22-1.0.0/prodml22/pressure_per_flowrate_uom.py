from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressurePerFlowrateUom(Enum):
    BAR_1000M3_DAY = "bar/(1000m3/day)"
    BAR_M3_DAY = "bar/(m3/day)"
    PA_1000M3_DAY = "Pa/(1000m3/day)"
    PA_M3_DAY = "Pa/(m3/day)"
    PSI_1000000FT3_DAY = "psi/(1000000ft3/day)"
    PSI_1000FT3_DAY = "psi/(1000ft3/day)"
    PSI_BBL_DAY = "psi/(bbl/day)"
