from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.legacy_mass_per_volume_uom import LegacyMassPerVolumeUom
from prodml22.mass_per_volume_uom import MassPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MassPerVolumeUom, str, LegacyMassPerVolumeUom]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
