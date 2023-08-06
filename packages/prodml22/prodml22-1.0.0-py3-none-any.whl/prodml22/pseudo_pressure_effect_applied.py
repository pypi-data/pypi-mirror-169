from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PseudoPressureEffectApplied(Enum):
    """Recurring enum used to list all the transforms which have been included
    in the pseudo pressure transform.

    If "Other" is selected, a comment should be used to explain.
    """
    GAS_PROPERTIES_WITH_PRESSURE = "gas properties with pressure"
    MULTIPHASE_FLOW_PROPERTIES_WITH_PRESSURE = "multiphase flow properties with pressure"
    OTHER = "other"
    VARIABLE_DESORPTION_WITH_PRESSURE = "variable desorption with pressure"
    VARIABLE_POROPERM_WITH_PRESSURE = "variable poroperm with pressure"
