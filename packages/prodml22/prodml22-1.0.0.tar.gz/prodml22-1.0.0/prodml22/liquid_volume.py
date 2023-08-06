from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_liquid_dropout_perc_volume import AbstractLiquidDropoutPercVolume
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LiquidVolume(AbstractLiquidDropoutPercVolume):
    """
    The amount of liquid by volume.

    :ivar liquid_volume: The amount of liquid by volume for this test
        step.
    """
    liquid_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LiquidVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
