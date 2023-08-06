from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.electromagnetic_moment_uom import ElectromagneticMomentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectromagneticMomentMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ElectromagneticMomentUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
