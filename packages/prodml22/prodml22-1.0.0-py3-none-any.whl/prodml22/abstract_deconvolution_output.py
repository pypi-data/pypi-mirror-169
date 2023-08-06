from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractDeconvolutionOutput:
    """Forces a choice between: in some deconvolution methods, multiple
    individual deconvolution outputs are generated, each specific to a
    corresponding individual Test Period.

    In such cases multiple instances of the deconvolutionOutput element
    will recur. In other cases, there will be only one such output
    across all Test Periods.
    """
