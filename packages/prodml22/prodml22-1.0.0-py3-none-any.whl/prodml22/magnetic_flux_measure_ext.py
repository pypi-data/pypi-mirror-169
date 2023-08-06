from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.magnetic_flux_uom import MagneticFluxUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticFluxMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MagneticFluxUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
