from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.molar_energy_uom import MolarEnergyUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MolarEnergyMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MolarEnergyUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
