from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_compositional_viscosity_model import AbstractCompositionalViscosityModel
from prodml22.prsv_parameter import PrsvParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FrictionTheory(AbstractCompositionalViscosityModel):
    """
    Friction theory.

    :ivar prsv_parameter: PRSV parameter.
    """
    prsv_parameter: List[PrsvParameter] = field(
        default_factory=list,
        metadata={
            "name": "PrsvParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
