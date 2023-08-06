from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.pressure_measure_ext import PressureMeasureExt
from prodml22.saturation_point_kind import SaturationPointKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SaturationPressure(PressureMeasureExt):
    """
    Saturation pressure.

    :ivar kind: The kind of saturation point whose pressure is being
        measured. Enum. See saturationpointkind.
    """
    kind: Optional[SaturationPointKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
