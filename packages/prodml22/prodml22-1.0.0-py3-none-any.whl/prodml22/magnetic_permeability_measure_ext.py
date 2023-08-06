from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.magnetic_permeability_uom import MagneticPermeabilityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticPermeabilityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MagneticPermeabilityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
