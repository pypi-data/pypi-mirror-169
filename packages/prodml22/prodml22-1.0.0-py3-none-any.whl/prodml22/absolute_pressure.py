from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.pressure_measure_ext import PressureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbsolutePressure(AbstractPressureValue):
    absolute_pressure: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "AbsolutePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
