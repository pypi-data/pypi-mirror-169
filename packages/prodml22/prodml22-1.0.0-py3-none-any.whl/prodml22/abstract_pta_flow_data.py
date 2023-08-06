from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_flow_test_data import AbstractFlowTestData
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_phase_kind import FluidPhaseKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractPtaFlowData(AbstractFlowTestData):
    """
    Actual measured flow data.

    :ivar fluid_phase_measured_kind: An enum of which phases are being
        measured by this flow data Channel.
    :ivar flow_channel: The Channel containing the Flow data.
    """
    fluid_phase_measured_kind: Optional[FluidPhaseKind] = field(
        default=None,
        metadata={
            "name": "FluidPhaseMeasuredKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flow_channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowChannel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
