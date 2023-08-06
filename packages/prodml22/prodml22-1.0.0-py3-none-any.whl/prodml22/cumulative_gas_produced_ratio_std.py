from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_gas_produced_ratio_volume import AbstractGasProducedRatioVolume
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CumulativeGasProducedRatioStd(AbstractGasProducedRatioVolume):
    """
    The standard condition of cumulative gas produced ratio.

    :ivar cumulative_gas_produced_ratio_std: The standard condition of
        cumulative gas produced ratio.
    """
    cumulative_gas_produced_ratio_std: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeGasProducedRatioStd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
