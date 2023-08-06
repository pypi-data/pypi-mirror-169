from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.angular_acceleration_uom import AngularAccelerationUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AngularAccelerationMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[AngularAccelerationUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
