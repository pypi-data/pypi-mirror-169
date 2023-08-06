from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.product_flow_change_log import ProductFlowChangeLog
from prodml22.product_flow_external_port import ProductFlowExternalPort
from prodml22.product_flow_network_plan import ProductFlowNetworkPlan
from prodml22.product_flow_unit import ProductFlowUnit

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowNetwork:
    """
    The non-contextual content of a product flow network object.

    :ivar name: The name of the product flow network. This must be
        unique within the context of the overall product flow model.
    :ivar plan_name: The name of a network plan. This indicates a
        planned network. All child network components must all be
        planned and be part of the same plan. The parent network must
        either contain the plan (i.e., be an actual) or be part of the
        same plan. Not specified indicates an actual network.
    :ivar parent_network_reference: A pointer to the network containing
        the unit that this network represents. That is, the unit must
        exist in a different network. If a parent network is not
        specified then the network represents the model. A model should
        only be represented by one network. The model network represents
        the overall installation. All other networks represent internal
        detail and should not be referenced from outside the model. The
        external ports on the model network represent the external ports
        to the overall product flow model. A pointer to an external port
        on the product flow model does not require the name of the model
        network because it is redundant to knowledge of the model name
        (i.e., there is a one-to-one correspondence).
    :ivar comment: A descriptive remark about the network.
    :ivar port: An external port. This exposes an internal node for the
        purpose of allowing connections to the internal behavior of the
        network. Networks that represent a Flow Unit should always have
        external ports. If this network represents a Unit then the name
        of the external port must match the name of a port on the Unit
        (i.e., they are logically the same port).
    :ivar plan: Defines the existance of a planned network which is a
        variant of this network beginning at a specified point in time.
        Any changes to the actual network after that time do not affect
        the plan.
    :ivar change_log: Documents that a change occurred at a particular
        time.
    :ivar unit: A flow behavior for one unit. Within this context, a
        unit represents a usage of equipment for some purpose. The unit
        is generally identified by its function rather than the actual
        equipment used to realize the function. A unit might represent
        something complex like a field or separator or something simple
        like a valve or pump.
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
    plan_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    parent_network_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentNetworkReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    port: List[ProductFlowExternalPort] = field(
        default_factory=list,
        metadata={
            "name": "Port",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    plan: List[ProductFlowNetworkPlan] = field(
        default_factory=list,
        metadata={
            "name": "Plan",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    unit: List[ProductFlowUnit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
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
