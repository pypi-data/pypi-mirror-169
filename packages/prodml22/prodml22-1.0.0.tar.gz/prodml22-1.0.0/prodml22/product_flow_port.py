from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.connected_node import ConnectedNode
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.name_struct import NameStruct
from prodml22.product_flow_expected_unit_property import ProductFlowExpectedUnitProperty
from prodml22.product_flow_port_type import ProductFlowPortType
from prodml22.product_flow_qualifier_expected import ProductFlowQualifierExpected

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowPort:
    """
    Product Flow Port Schema.

    :ivar direction: Defines whether this port is an inlet or outlet.
        This is a nominal intended direction.
    :ivar name: The name of the port within the context of the product
        flow unit.
    :ivar plan_name: The name of a network plan. This indicates a
        planned port. All child network components must all be planned
        and be part of the same plan. The parent unit must be part of
        the same plan or be an actual. Not specified indicates an actual
        port.
    :ivar facility: The name of the facility represented by this
        ProductFlowPort The name can be qualified by a naming system.
        The facility name is assumed to be unique within the context of
        the facility represented by the unit. This also defines the kind
        of facility.
    :ivar facility_alias: An alternative name of a facility. This is
        generally unique within a naming system. The above contextually
        unique name should also be listed as an alias.
    :ivar exposed: True ("true" or "1") indicates that the port is an
        exposed internal port and cannot be used in a connection
        external to the unit. False ("false" or "0") or not given
        indicates a normal port.
    :ivar comment: A descriptive remark associated with this port.
    :ivar connected_node: Defines the node to which this port is
        connected. A timestamp activates and deactivates the connection.
        Only one connectedNode should be active at any one point in
        time. There are no semantics for the node except common
        connection. All ports that are connected to a node with the the
        same name are inherently connected to each other. The name of
        the node is only required to be unique within the context of the
        current Product Flow Network (that is, not the overall model).
        All ports must be connected to a node and whether or not any
        other port is connected to the same node depends on the
        requirements of the network. Any node that is internally
        connected to only one port is presumably a candidate to be
        connected to an external node. The behavior of ports connected
        at a common node is as follows: a) There is no pressure drop
        across the node. All ports connected to the node have the same
        pressure. That is, there is an assumption of steady state fluid
        flow. b) Conservation of mass exists across the node. The mass
        into the node via all connected ports equals the mass out of the
        node via all connected ports. c) The flow direction of a port
        connected to the node may be transient. That is, flow direction
        may change toward any port(s) if the relative internal pressure
        of the Product Flow Units change and a new steady state is
        achieved.
    :ivar expected_flow_property: Defines the properties that are
        expected to be measured at this port. This can also specify the
        equipment tag(s) of the sensor that will read the value. Only
        one of each property kind should be active at any point in time.
    :ivar expected_flow_product: Defines the expected flow and product
        pairs to be assigned to this port by a Product Volume report. A
        set of expected qualifiers can be defined for each pair.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    direction: Optional[ProductFlowPortType] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
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
    facility: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    facility_alias: List[NameStruct] = field(
        default_factory=list,
        metadata={
            "name": "FacilityAlias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    connected_node: List[ConnectedNode] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedNode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    expected_flow_property: List[ProductFlowExpectedUnitProperty] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedFlowProperty",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    expected_flow_product: List[ProductFlowQualifierExpected] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedFlowProduct",
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
