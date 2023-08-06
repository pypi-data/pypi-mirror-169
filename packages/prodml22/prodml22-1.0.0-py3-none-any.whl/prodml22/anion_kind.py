from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class AnionKind(Enum):
    B_OH_4 = "B(OH)4-"
    BR = "Br-"
    CL = "Cl-"
    CO3_2 = "CO3-2"
    F = "F-"
    HCO3 = "HCO3-"
    HS = "HS-"
    I = "I-"
    NO2 = "NO2-"
    NO3_2 = "NO3-2"
    OH = "OH-"
    PO4_3 = "PO4-3"
    S_2 = "S-2"
    SO4_2 = "SO4-2"
