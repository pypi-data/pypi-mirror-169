from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.time_per_mass_uom import TimePerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimePerMassMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[TimePerMassUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
