from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.deconvolved_pressure_data import DeconvolvedPressureData
from prodml22.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeconvolutionOutput:
    """
    This contains the output curves from a deconvolution.

    :ivar deconvolved_pressure: The result of deconvolution: a
        deconvolved pressure which corresponds to the constant rate
        drawdown response at the reference flow condition.
    :ivar deconvolution_reference_flowrate_value: The reference flow
        condition at which the corresponding deconvolved pressure
        constant drawdown response is calculated.
    """
    deconvolved_pressure: Optional[DeconvolvedPressureData] = field(
        default=None,
        metadata={
            "name": "DeconvolvedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    deconvolution_reference_flowrate_value: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "DeconvolutionReferenceFlowrateValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
