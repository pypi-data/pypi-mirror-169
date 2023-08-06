from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeltaPressureTotalSkin(AbstractParameter):
    """The pressure drop caused by the total skin factor.

    Equal to the difference in pressure at the wellbore between what was
    observed at a flowrate and what would be observed if the radial flow
    regime in the reservoir persisted right into the wellbore. The
    reference flowrate will be the stable flowrate used to analyse a
    drawdown, or the stable last flowrate preceding a buildup.
    """
    abbreviation: str = field(
        init=False,
        default="dP Skin",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
