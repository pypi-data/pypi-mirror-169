from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.attenuation_per_frequency_interval_uom import AttenuationPerFrequencyIntervalUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AttenuationPerFrequencyIntervalMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AttenuationPerFrequencyIntervalUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
