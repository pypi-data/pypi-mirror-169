from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_attenuation_measure import AbstractAttenuationMeasure
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaveLength(AbstractAttenuationMeasure):
    """
    Wave length.

    :ivar wave_length: Wave length.
    """
    wave_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "WaveLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
