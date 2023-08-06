from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_gas_produced_ratio_volume import AbstractGasProducedRatioVolume
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CumulativeGasProducedVol(AbstractGasProducedRatioVolume):
    """
    The cumulative gas produced volume.

    :ivar cumulative_gas_produced_volume: The cumulative gas oil
        produced ratio at standard conditions.
    """
    cumulative_gas_produced_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeGasProducedVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
