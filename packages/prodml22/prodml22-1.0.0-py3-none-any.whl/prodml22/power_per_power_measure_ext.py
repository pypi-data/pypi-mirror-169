from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.power_per_power_uom import PowerPerPowerUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PowerPerPowerMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[PowerPerPowerUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
