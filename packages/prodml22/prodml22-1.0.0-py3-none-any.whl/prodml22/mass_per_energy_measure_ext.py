from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.mass_per_energy_uom import MassPerEnergyUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerEnergyMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MassPerEnergyUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
