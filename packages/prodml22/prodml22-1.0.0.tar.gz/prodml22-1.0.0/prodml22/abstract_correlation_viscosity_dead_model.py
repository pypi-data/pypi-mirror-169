from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_model import AbstractCorrelationViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationViscosityDeadModel(AbstractCorrelationViscosityModel):
    """
    Abstract class of correlation viscosity dead model.

    :ivar dead_oil_viscosity: The dead oil viscosity output from the
        dead oil viscosity model.
    :ivar reservoir_temperature: The reservoir temperature for the dead
        oil viscosity model.
    """
    dead_oil_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "DeadOilViscosity",
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
