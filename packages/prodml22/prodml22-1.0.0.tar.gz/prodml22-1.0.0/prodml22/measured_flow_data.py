from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MeasuredFlowData(AbstractPtaFlowData):
    """
    Pressure data measured during the flow test.
    """
