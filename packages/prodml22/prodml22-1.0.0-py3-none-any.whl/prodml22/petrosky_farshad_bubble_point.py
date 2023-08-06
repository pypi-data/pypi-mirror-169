from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_correlation_viscosity_bubble_point_model import AbstractCorrelationViscosityBubblePointModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PetroskyFarshadBubblePoint(AbstractCorrelationViscosityBubblePointModel):
    """
    PetroskyFarshad-BubblePoint.
    """
    class Meta:
        name = "PetroskyFarshad-BubblePoint"
