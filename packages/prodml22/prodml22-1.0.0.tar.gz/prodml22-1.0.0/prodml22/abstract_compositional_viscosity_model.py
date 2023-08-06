from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_compositional_model import AbstractCompositionalModel
from prodml22.thermodynamic_phase import ThermodynamicPhase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCompositionalViscosityModel(AbstractCompositionalModel):
    """
    Abstract class of compositional viscosity model.

    :ivar phase: The phase the compositional viscosity model applies to.
    """
    phase: Optional[ThermodynamicPhase] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
