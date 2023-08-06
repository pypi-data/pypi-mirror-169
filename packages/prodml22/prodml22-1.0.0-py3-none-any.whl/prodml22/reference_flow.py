from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_ref_product_flow import AbstractRefProductFlow

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReferenceFlow(AbstractRefProductFlow):
    """
    Reference flow.

    :ivar flow_reference: A pointer to the flow within the facility.
    """
    flow_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
