from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_interval import AbstractInterval
from prodml22.thermodynamic_temperature_measure_ext import ThermodynamicTemperatureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TemperatureInterval(AbstractInterval):
    min_temperature: Optional[ThermodynamicTemperatureMeasureExt] = field(
        default=None,
        metadata={
            "name": "MinTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    max_temperature: Optional[ThermodynamicTemperatureMeasureExt] = field(
        default=None,
        metadata={
            "name": "MaxTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
