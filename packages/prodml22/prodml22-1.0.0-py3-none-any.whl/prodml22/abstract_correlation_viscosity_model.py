from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_model import AbstractCorrelationModel
from prodml22.molecular_weight_measure import MolecularWeightMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationViscosityModel(AbstractCorrelationModel):
    """
    Abstract class of correlation viscosity  model.

    :ivar molecular_weight: The molecular weight of the fluid for the
        viscosity model.
    """
    molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "MolecularWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
