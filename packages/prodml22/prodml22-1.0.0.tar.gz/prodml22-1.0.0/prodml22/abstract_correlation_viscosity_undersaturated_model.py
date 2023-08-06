from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_model import AbstractCorrelationViscosityModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationViscosityUndersaturatedModel(AbstractCorrelationViscosityModel):
    """
    Abstract class of viscosity under-saturated model.

    :ivar undersaturated_oil_viscosity: The under saturated viscosity
        output from the under saturated viscosity model.
    :ivar bubble_point_oil_viscosity: The bubble point viscosity input
        for the under saturated viscosity model.
    :ivar bubble_point_pressure: The bubble point pressure for the under
        saturated viscosity model.
    :ivar pressure: The pressure for the under saturated viscosity
        model.
    """
    undersaturated_oil_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "UndersaturatedOilViscosity",
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
    bubble_point_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BubblePointPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
