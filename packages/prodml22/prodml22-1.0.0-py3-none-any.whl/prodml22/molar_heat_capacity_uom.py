from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MolarHeatCapacityUom(Enum):
    """
    :cvar BTU_IT_LBMOL_DELTA_F: BTU per pound-mass-mole delta Fahrenheit
    :cvar CAL_TH_MOL_DELTA_C: calorie per gram-mole delta Celsius
    :cvar J_MOL_DELTA_K: joule per gram-mole delta kelvin
    :cvar K_J_KMOL_DELTA_K: kilojoule per kilogram-mole delta kelvin
    """
    BTU_IT_LBMOL_DELTA_F = "Btu[IT]/(lbmol.deltaF)"
    CAL_TH_MOL_DELTA_C = "cal[th]/(mol.deltaC)"
    J_MOL_DELTA_K = "J/(mol.deltaK)"
    K_J_KMOL_DELTA_K = "kJ/(kmol.deltaK)"
