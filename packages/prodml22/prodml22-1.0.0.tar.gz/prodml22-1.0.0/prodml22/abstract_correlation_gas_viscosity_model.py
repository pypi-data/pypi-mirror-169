from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_model import AbstractCorrelationViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationGasViscosityModel(AbstractCorrelationViscosityModel):
    """
    Abstract class of correlation gas viscosity model.

    :ivar gas_viscosity: The gas viscosity output from the gas viscosity
        model.
    :ivar reservoir_temperature: The reservoir temperature for the gas
        viscosity model.
    """
    gas_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "GasViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reservoir_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReservoirTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
