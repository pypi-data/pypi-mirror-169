from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ThermodynamicPhase(Enum):
    """
    Specifies the thermodynamic phases.

    :cvar AQUEOUS: A water-rich liquid phase.
    :cvar OLEIC: An oil-rich liquid phase.
    :cvar VAPOR: A gaseous phase at the conditions present.
    :cvar TOTAL_HYDROCARBON: A phase comprised of the total hydrocarbons
        (e.g., above the critical pressure for a gas condensate).
    """
    AQUEOUS = "aqueous"
    OLEIC = "oleic"
    VAPOR = "vapor"
    TOTAL_HYDROCARBON = "total hydrocarbon"
