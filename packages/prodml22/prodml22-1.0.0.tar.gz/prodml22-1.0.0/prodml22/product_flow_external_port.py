from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.product_flow_port_type import ProductFlowPortType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowExternalPort:
    """
    Product Flow Network External Port Schema.

    :ivar name: The name of the external port within the context of the
        current product flow network.
    :ivar direction: Defines whether this port is an inlet or outlet.
        Note that this is a nominal intended direction.
    :ivar exposed: True ("true" or "1") indicates that the port is an
        exposed internal port and cannot be used in a connection
        external to the network. False ("false" or "0") or not given
        indicates a normal port.
    :ivar connected_node: Defines the internal node to which this
        external port is connected. All ports (whether internal or
        external) that are connected to a node with the same name are
        connected to each other. Node names are unique to each network.
        The purpose of the external port is to provide input to or
        output from the internal network except when the port is an
        "exposed" port. The purpose of an exposed port is to allow the
        properties of the port to be seen external to the network. For
        an exposed port, the connection points to the associated port.
    :ivar comment: A descriptive remark about the port.
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
    direction: Optional[ProductFlowPortType] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    exposed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exposed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    connected_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectedNode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
