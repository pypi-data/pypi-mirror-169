from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.linear_acceleration_uom import LinearAccelerationUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LinearAccelerationMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LinearAccelerationUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
