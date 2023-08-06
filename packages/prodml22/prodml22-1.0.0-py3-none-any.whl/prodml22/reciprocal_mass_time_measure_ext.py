from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.reciprocal_mass_time_uom import ReciprocalMassTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalMassTimeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ReciprocalMassTimeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
