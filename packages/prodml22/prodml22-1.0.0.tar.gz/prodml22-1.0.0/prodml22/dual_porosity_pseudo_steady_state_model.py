from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.interporosity_flow_parameter import InterporosityFlowParameter
from prodml22.reservoir_base_model import ReservoirBaseModel
from prodml22.storativity_ratio import StorativityRatio

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DualPorosityPseudoSteadyStateModel(ReservoirBaseModel):
    """
    Dual Porosity reservoir model, with Pseudo-Steady-State flow between the
    two porosity systems.
    """
    interporosity_flow_parameter: Optional[InterporosityFlowParameter] = field(
        default=None,
        metadata={
            "name": "InterporosityFlowParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    storativity_ratio: Optional[StorativityRatio] = field(
        default=None,
        metadata={
            "name": "StorativityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
