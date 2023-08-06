from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_compositional_model import AbstractCompositionalModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCompositionalEoSmodel(AbstractCompositionalModel):
    """
    Abstract class of compositional EoS model.
    """
    class Meta:
        name = "AbstractCompositionalEoSModel"
