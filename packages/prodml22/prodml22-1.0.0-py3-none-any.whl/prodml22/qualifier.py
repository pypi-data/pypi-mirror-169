from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.expected_flow_qualifier import ExpectedFlowQualifier
from prodml22.flow_qualifier import FlowQualifier

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Qualifier(ExpectedFlowQualifier):
    """
    :ivar qualifier: The expected kind of qualifier of the property.
        This element should only be specified for properties that do not
        represent the fluid stream (e.g., a valve status).
    """
    qualifier: List[FlowQualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
