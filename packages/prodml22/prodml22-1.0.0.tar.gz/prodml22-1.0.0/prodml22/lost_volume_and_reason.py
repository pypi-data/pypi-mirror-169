from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.reason_lost import ReasonLost
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LostVolumeAndReason(VolumeMeasure):
    """
    A volume corrected to standard temperature and pressure.

    :ivar reason_lost: Defines why the volume was lost.
    """
    reason_lost: Optional[ReasonLost] = field(
        default=None,
        metadata={
            "name": "reasonLost",
            "type": "Attribute",
            "required": True,
        }
    )
