from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_compositional_eo_smodel import AbstractCompositionalEoSmodel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SrkEos(AbstractCompositionalEoSmodel):
    """
    Srk_EOS.
    """
    class Meta:
        name = "Srk_EOS"
