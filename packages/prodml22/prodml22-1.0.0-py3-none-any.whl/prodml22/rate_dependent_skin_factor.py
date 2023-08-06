from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.time_per_volume_measure_ext import TimePerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RateDependentSkinFactor(AbstractParameter):
    """Value characterizing the rate at which an apparent skin effect, due to
    additional pressure drop, due to turbulent flow, grows as a function of
    flowrate.

    The additional flowrate-dependent Skin is this value D * Flowrate. The total measured Skin factor would then be S + DQ, where Q is the flowrate.
    """
    abbreviation: str = field(
        init=False,
        default="D",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    inverse_flowrate: Optional[TimePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "InverseFlowrate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
