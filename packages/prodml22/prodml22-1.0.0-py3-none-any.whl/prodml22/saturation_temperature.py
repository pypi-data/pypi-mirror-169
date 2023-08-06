from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.saturation_point_kind import SaturationPointKind
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SaturationTemperature(ThermodynamicTemperatureMeasure):
    """
    Saturation temperature.

    :ivar kind: The kind of saturation point whose temperature is being
        measured. Enum. See saturationpointkind.
    """
    kind: Optional[SaturationPointKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
