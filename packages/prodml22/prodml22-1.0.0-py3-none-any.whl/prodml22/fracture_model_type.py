from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FractureModelType(Enum):
    COMPRESSIBLE_FINITE_CONDUCTIVITY = "compressible finite conductivity"
    FINITE_CONDUCTIVITY = "finite conductivity"
    INFINITE_CONDUCTIVITY = "infinite conductivity"
    UNIFORM_FLUX = "uniform flux"
