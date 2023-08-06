from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ViscosityAtTemperature:
    """
    Viscosity measurement at a specific temperature.

    :ivar viscosity: Viscosity measurement at the associated
        temperature.
    :ivar viscosity_temperature: Temperature at which the viscosity was
        measured.
    """
    viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "Viscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    viscosity_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ViscosityTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
