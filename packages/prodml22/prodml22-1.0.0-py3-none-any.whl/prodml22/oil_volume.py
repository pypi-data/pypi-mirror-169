from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_oil_vol_shrinkage import AbstractOilVolShrinkage
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OilVolume(AbstractOilVolShrinkage):
    """
    Oil volume.

    :ivar oil_volume: The volume of oil.
    """
    oil_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
