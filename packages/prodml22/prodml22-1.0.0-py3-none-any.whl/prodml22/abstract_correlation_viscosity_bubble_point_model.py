from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_model import AbstractCorrelationViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationViscosityBubblePointModel(AbstractCorrelationViscosityModel):
    """
    Abstract class of viscosity bubble point model.

    :ivar dead_oil_viscosity: The dead oil viscosity input for the
        bubble point viscosity model.
    :ivar bubble_point_oil_viscosity: The bubble point viscosity output
        from the bubble point viscosity model.
    :ivar solution_gas_oil_ratio: The solution gas oil ratio for the
        bubble point viscosity model.
    """
    dead_oil_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "DeadOilViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bubble_point_oil_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "BubblePointOilViscosity",
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
