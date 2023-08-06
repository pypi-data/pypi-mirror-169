from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_correlation_viscosity_undersaturated_model import AbstractCorrelationViscosityUndersaturatedModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class BerganAndSuttonUndersaturated(AbstractCorrelationViscosityUndersaturatedModel):
    """
    Bergan And Sutton-Undersaturated.
    """
    class Meta:
        name = "BerganAndSutton-Undersaturated"
