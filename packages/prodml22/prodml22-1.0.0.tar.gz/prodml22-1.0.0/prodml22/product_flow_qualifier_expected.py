from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.expected_flow_qualifier import ExpectedFlowQualifier
from prodml22.flow_qualifier import FlowQualifier
from prodml22.reporting_flow import ReportingFlow
from prodml22.reporting_product import ReportingProduct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowQualifierExpected(ExpectedFlowQualifier):
    """
    Defines an expected combination of kinds.

    :ivar flow: The expected kind of flow.
    :ivar product: The expected kind of product within the flow.
    :ivar qualifier: The expected kind of qualifier of the flow.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    flow: Optional[ReportingFlow] = field(
        default=None,
        metadata={
            "name": "Flow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    product: Optional[ReportingProduct] = field(
        default=None,
        metadata={
            "name": "Product",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    qualifier: List[FlowQualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
