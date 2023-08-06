from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConnectedNode:
    """
    Product Flow Connected Node Schema.

    :ivar node: Defines the node to which this port is connected. Only
        two ports should be actively connected to the same node at the
        same point in time. That is, a port should only be connected to
        one other port. There are no semantics for the node except
        common connection. All ports that are connected to a node with
        the same name are inherently connected to each other. The name
        of the node is only required to be unique within the context of
        the current Product Flow Network (that is, not the overall
        model). All ports must be connected to a node and whether or not
        any other port is connected to the same node depends on the
        requirements of the network. Any node that is internally
        connected to only one node is presumably a candidate to be
        connected to an external node. The behavior of ports connected
        at a common node is as follows: a) There is no pressure drop
        across the node. All ports connected to the node have the same
        pressure. That is, there is an assumption of steady state fluid
        flow. b) Conservation of mass exists across the node. The mass
        into the node via all connected ports equals the mass out of the
        node via all connected ports. c) The flow direction of a port
        connected to the node may be transient. That is, flow direction
        may change toward any port if the relative internal pressure of
        the Product Flow Units change and a new steady state is
        achieved.
    :ivar plan_name: The name of a network plan. This indicates a
        planned connection. The connected port must be part of the same
        plan or be an actual. Not specified indicates an actual
        connection.
    :ivar dtim_start: The date and time that the connection was
        activated.
    :ivar dtim_end: The date and time that the connection was
        terminated.
    :ivar comment: A descriptive remark associated with this connection,
        possibly including a reason for termination.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "name": "Node",
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
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
