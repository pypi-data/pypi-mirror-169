from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RelativeVolumeRatio(VolumePerVolumeMeasure):
    """Contains a relative volume (ie volume/reference volume), and the
    identity of the reference volume and/or volume measurement conditions, by
    means of a uid.

    This uid will correspond to the uid of the appropriate Fluid Volume
    Reference.

    :ivar fluid_volume_reference: Reference to a fluid volume.
    """
    fluid_volume_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidVolumeReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
