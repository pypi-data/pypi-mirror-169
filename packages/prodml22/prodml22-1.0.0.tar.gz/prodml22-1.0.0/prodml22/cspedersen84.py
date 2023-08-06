from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_compositional_viscosity_model import AbstractCompositionalViscosityModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Cspedersen84(AbstractCompositionalViscosityModel):
    """
    CSPedersen84.
    """
    class Meta:
        name = "CSPedersen84"
