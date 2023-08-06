from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractLiquidDropoutPercVolume:
    """
    Provide either the liquid volume, or the liquid dropout percent, which is
    the liquid volume divided by the total volume.
    """
