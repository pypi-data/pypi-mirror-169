from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_correlation_gas_viscosity_model import AbstractCorrelationGasViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.pvt_model_parameter import PvtModelParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LondonoArcherBlasinggame(AbstractCorrelationGasViscosityModel):
    """
    LondonoArcherBlasinggame.

    :ivar gas_density: The gas density at the conditions for this
        viscosity correlation to be used.
    :ivar gas_viscosity_at1_atm: The gas viscosity at 1 atm for the
        viscosity correlation.
    :ivar gas_viscosity_coefficient1_atm:
    """
    gas_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasDensity",
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
    gas_viscosity_coefficient1_atm: List[PvtModelParameter] = field(
        default_factory=list,
        metadata={
            "name": "GasViscosityCoefficient1Atm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
