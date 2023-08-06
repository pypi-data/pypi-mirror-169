from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_liquid_dropout_perc_volume import AbstractLiquidDropoutPercVolume
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LiquidDropoutFraction(AbstractLiquidDropoutPercVolume):
    """
    The fraction of liquid by volume.

    :ivar liquid_dropout_percent: The fraction of liquid by volume for
        this test step.
    """
    liquid_dropout_percent: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LiquidDropoutPercent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
