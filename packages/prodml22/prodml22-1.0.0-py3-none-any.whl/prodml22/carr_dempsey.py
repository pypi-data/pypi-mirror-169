from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_gas_viscosity_model import AbstractCorrelationGasViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.pressure_per_pressure_measure import PressurePerPressureMeasure
from prodml22.thermodynamic_temperature_per_thermodynamic_temperature_measure import ThermodynamicTemperaturePerThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CarrDempsey(AbstractCorrelationGasViscosityModel):
    """
    CarrDempsey.

    :ivar gas_molar_weight: The molecular weight of the gas as an input
        to this viscosity correlation.
    :ivar gas_viscosity_at1_atm: The gas viscosity at 1 atm for the
        viscosity correlation.
    :ivar pseudo_reduced_temperature: The pseudo reducedtemperature for
        the viscosity correlation.
    :ivar pseudo_reduced_pressure: The pseudo reduced pressure for the
        viscosity correlation.
    """
    gas_molar_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GasMolarWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_viscosity_at1_atm: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "GasViscosityAt1Atm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pseudo_reduced_temperature: Optional[ThermodynamicTemperaturePerThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "PseudoReducedTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pseudo_reduced_pressure: Optional[PressurePerPressureMeasure] = field(
        default=None,
        metadata={
            "name": "PseudoReducedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
