from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_oil_vol_shrinkage import AbstractOilVolShrinkage
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OilShrinkageFactor(AbstractOilVolShrinkage):
    """
    Oil shrinkage factor.

    :ivar oil_shrinkage_factor: The oil shrinkage factor.
    """
    oil_shrinkage_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilShrinkageFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
