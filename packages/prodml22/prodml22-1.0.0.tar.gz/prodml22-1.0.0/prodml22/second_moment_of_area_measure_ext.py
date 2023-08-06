from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.second_moment_of_area_uom import SecondMomentOfAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class SecondMomentOfAreaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[SecondMomentOfAreaUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
