from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_undersaturated_model import AbstractCorrelationViscosityUndersaturatedModel
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DindorukChristmanUndersaturated(AbstractCorrelationViscosityUndersaturatedModel):
    """
    DindorukChristman-Undersaturated.

    :ivar reservoir_temperature: The reservoir temperature for the
        viscosity correlation.
    :ivar solution_gas_oil_ratio: The solution gas-oil ratio for the
        viscosity correlation.
    """
    class Meta:
        name = "DindorukChristman-Undersaturated"

    reservoir_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReservoirTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    solution_gas_oil_ratio: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolutionGasOilRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
