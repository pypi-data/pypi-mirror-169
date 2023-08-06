from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class OrganicAcidKind(Enum):
    COO_22 = "(COO)22-"
    C2_H5_OCOO = "C2H5OCOO-"
    C3_H5_O_COO_33 = "C3H5O(COO)33-"
    CH2_COO_22 = "CH2(COO)22-"
    CH2_OHCOO = "CH2OHCOO-"
    CH3_CH2_2_COO = "CH3(CH2)2COO-"
    CH3_CH2_3_COO = "CH3(CH2)3COO-"
    CH3_CH2_COO = "CH3CH2COO-"
    CH3_COO = "CH3COO-"
    HCOO = "HCOO-"
