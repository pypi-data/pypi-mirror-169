from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerVolumePerTemperatureUom(Enum):
    KG_M3_DEG_C = "kg/m3.degC"
    KG_M3_K = "kg/m3.K"
    LB_FT_DEG_F = "lb/ft.degF"
