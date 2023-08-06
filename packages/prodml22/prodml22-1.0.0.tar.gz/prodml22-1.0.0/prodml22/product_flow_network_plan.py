from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.product_flow_change_log import ProductFlowChangeLog

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowNetworkPlan:
    """
    A plan to extend an actual network.

    :ivar name: The name assigned to the plan.
    :ivar dtim_start: The date and time of the start of the plan. This
        point coincides with the end of the actual configuration. The
        configuration of the actual at this point in time represents the
        configuration of the plan at this starting point. All changes to
        this plan must be in the future from this point in time.
    :ivar purpose: A textual description of the purpose of the plan.
    :ivar change_log: Documents that a change occurred at a particular
        time.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    change_log: List[ProductFlowChangeLog] = field(
        default_factory=list,
        metadata={
            "name": "ChangeLog",
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
