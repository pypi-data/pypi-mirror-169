from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.pressure_measure_ext import PressureMeasureExt
from prodml22.reference_pressure import ReferencePressure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GaugePressure(AbstractPressureValue):
    gauge_pressure: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "GaugePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    reference_pressure: Optional[ReferencePressure] = field(
        default=None,
        metadata={
            "name": "ReferencePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
