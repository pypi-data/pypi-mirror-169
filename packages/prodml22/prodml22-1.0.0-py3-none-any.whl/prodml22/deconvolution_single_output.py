from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_deconvolution_output import AbstractDeconvolutionOutput
from prodml22.deconvolution_output import DeconvolutionOutput

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeconvolutionSingleOutput(AbstractDeconvolutionOutput):
    """
    This element is chosen when a single deconvolution output applies across
    all Test Periods.
    """
    deconvolution_single_output: Optional[DeconvolutionOutput] = field(
        default=None,
        metadata={
            "name": "DeconvolutionSingleOutput",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
