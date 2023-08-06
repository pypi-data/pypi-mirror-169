from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_attenuation_measure import AbstractAttenuationMeasure
from prodml22.frequency_measure import FrequencyMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Frequency(AbstractAttenuationMeasure):
    """
    Frequency.

    :ivar frequency: Frequency.
    """
    frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
