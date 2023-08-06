from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FluidPhaseKind(Enum):
    MULTIPHASE_GAS_WATER = "multiphase gas+water"
    MULTIPHASE_OIL_GAS = "multiphase oil+gas"
    MULTIPHASE_OIL_WATER = "multiphase oil+water"
    MULTIPHASE_OIL_WATER_GAS = "multiphase oil+water+gas"
    SINGLE_PHASE_GAS = "single phase gas"
    SINGLE_PHASE_OIL = "single phase oil"
    SINGLE_PHASE_WATER = "single phase water"
