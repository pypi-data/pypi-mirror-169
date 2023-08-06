from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData
from prodml22.abstract_rate_history import AbstractRateHistory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ChannelFlowrateData(AbstractRateHistory):
    """
    This choice should be made when the Rate History is a multiple rate
    history, ie a time series of flowrates.

    :ivar input_flowrate: Flow data.
    """
    input_flowrate: Optional[AbstractPtaFlowData] = field(
        default=None,
        metadata={
            "name": "InputFlowrate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
