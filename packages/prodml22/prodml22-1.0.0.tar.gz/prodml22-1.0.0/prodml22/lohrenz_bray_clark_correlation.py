from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_compositional_viscosity_model import AbstractCompositionalViscosityModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LohrenzBrayClarkCorrelation(AbstractCompositionalViscosityModel):
    """
    Lohrenz-Bray-ClarkCorrelation.
    """
    class Meta:
        name = "Lohrenz-Bray-ClarkCorrelation"
