from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_analysis import AbstractAnalysis
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.log_log_analysis import LogLogAnalysis
from prodml22.output_flow_data import OutputFlowData
from prodml22.specialized_analysis import SpecializedAnalysis

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RtaAnalysis(AbstractAnalysis):
    """
    Contains the input data needed for analysis of flowrate (RTA) (ie where
    pressure is the boundary condition).

    :ivar input_pressure: The pressure (in a Channel) which is being
        analysed in this RTA.
    :ivar input_flowrate_data: The flow rate (in a Channel) which is
        being analysed in this RTA.
    :ivar simulated_flowrate: The simulated flow rate (in a Channel)
        which is the output of this RTA.
    :ivar simulated_log_log_data:
    :ivar specialized_analysis:
    :ivar measured_log_log_data:
    """
    input_pressure: Optional[AbstractPtaPressureData] = field(
        default=None,
        metadata={
            "name": "InputPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    input_flowrate_data: Optional[AbstractPtaFlowData] = field(
        default=None,
        metadata={
            "name": "InputFlowrateData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    simulated_flowrate: Optional[OutputFlowData] = field(
        default=None,
        metadata={
            "name": "SimulatedFlowrate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    simulated_log_log_data: Optional[LogLogAnalysis] = field(
        default=None,
        metadata={
            "name": "SimulatedLogLogData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    specialized_analysis: List[SpecializedAnalysis] = field(
        default_factory=list,
        metadata={
            "name": "SpecializedAnalysis",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_log_log_data: Optional[LogLogAnalysis] = field(
        default=None,
        metadata={
            "name": "MeasuredLogLogData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
