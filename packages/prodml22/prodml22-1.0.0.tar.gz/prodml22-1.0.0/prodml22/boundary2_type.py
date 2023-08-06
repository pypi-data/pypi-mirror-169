from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class Boundary2Type(Enum):
    CONSTANT_PRESSURE = "constant pressure"
    NO_FLOW = "no-flow"
