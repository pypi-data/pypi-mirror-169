from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractAnalysis:
    """Forces a choice between pressure analysis (PTA) with flow as a boundary
    condition, and flowrate analysis (RTA) with pressure as a boundary
    condition.

    Applies to the measured data and to the simulation.
    """
