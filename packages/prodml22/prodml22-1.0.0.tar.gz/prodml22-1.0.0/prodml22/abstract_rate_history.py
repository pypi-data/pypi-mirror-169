from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractRateHistory:
    """
    Forces a choice between a single flowrate and producing time, or a time
    series of rates, for the Rate History of a pressure transient result.
    """
