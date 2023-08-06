from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.temperature_interval_uom import TemperatureIntervalUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TemperatureIntervalMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[TemperatureIntervalUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
