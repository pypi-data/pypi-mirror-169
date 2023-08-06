from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_deconvolution_output import AbstractDeconvolutionOutput
from prodml22.deconvolution_output import DeconvolutionOutput

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeconvolutionMultipleOutput(AbstractDeconvolutionOutput):
    """
    This element is chosen when separate individual deconvolution outputs apply
    to corresponding individual Test Periods.

    :ivar test_period_output_ref_id: Where deconvolution has been
        performed to generate deconvolved pressure over multiple time
        periods, this is the uid of the time period for this deconvolved
        pressure channel.
    :ivar deconvolution_multiple_output:
    """
    test_period_output_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestPeriodOutputRefId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    deconvolution_multiple_output: Optional[DeconvolutionOutput] = field(
        default=None,
        metadata={
            "name": "DeconvolutionMultipleOutput",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
