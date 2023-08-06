from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_gas_viscosity_model import AbstractCorrelationGasViscosityModel
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LeeGonzalez(AbstractCorrelationGasViscosityModel):
    """
    LeeGonzalez.

    :ivar gas_molar_weight: The molecular weight of the gas as an input
        to this viscosity correlation.
    :ivar gas_density: The gas density at the conditions for this
        viscosity correlation to be used.
    """
    gas_molar_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GasMolarWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
