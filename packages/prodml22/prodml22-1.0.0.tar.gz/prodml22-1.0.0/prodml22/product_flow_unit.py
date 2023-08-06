from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.name_struct import NameStruct
from prodml22.product_flow_expected_unit_property import ProductFlowExpectedUnitProperty
from prodml22.product_flow_port import ProductFlowPort
from prodml22.relative_coordinate import RelativeCoordinate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowUnit:
    """
    Product Flow Unit Schema.

    :ivar name: The name of the ProductFlowUnit within the context of
        the ProductFlowNetwork.
    :ivar plan_name: The name of a network plan. This indicates a
        planned unit. All child network components must all be planned
        and be part of the same plan. The parent network must either
        contain the plan (i.e., be an actual) or be part of the same
        plan. Not specified indicates an actual unit.
    :ivar internal_network_reference: A pointer to the network
        representing the internal behavior of this unit. The names of
        the external ports on the internal network must match the names
        of the ports on this unit. That is they are logically the same
        ports.
    :ivar facility: The name of the facility for which this Product Flow
        Unit describes fluid flow connection behavior. The name can be
        qualified by a naming system. This also defines the kind of
        facility.
    :ivar facility_parent1: For facilities whose name is unique within
        the context of another facility, the name of the parent facility
        this named facility. The name can be qualified by a naming
        system. This also defines the kind of facility.
    :ivar facility_parent2: For facilities whose name is unique within
        the context of another facility, the name of the parent facility
        of facilityParent1. The name can be qualified by a naming
        system. This also defines the kind of facility.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented facility.
    :ivar comment: A descriptive remark associated with this unit.
    :ivar expected_property: Defines an expected property of the
        facility represented by this unit.
    :ivar port: An inlet or outlet port associated with this unit. If
        there is an internal network then the name of this port must
        match the name of an external port for that network. Any
        properties (e.g., volume, pressure, temperature) that are
        assigned to this port are inherently assigned to the
        corresponding external port on the internal network. That is,
        the ports are logically the same port. Similar to a node, there
        is no pressure drop across a port. Also similar to a node,
        conservation of mass exists across the port and the flow
        direction across the port can change over time if the relative
        pressures across connected units change.
    :ivar relative_coordinate: Defines the relative coordinate of the
        unit on a display screen. This is not intended for detailed
        diagrams. Rather it is intended to allow different applications
        to present a user view which has a consistent layout.
    :ivar facility_alias:
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
    internal_network_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternalNetworkReference",
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
    facility_parent1: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    facility_parent2: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    context_facility: List[FacilityIdentifierStruct] = field(
        default_factory=list,
        metadata={
            "name": "ContextFacility",
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
    expected_property: List[ProductFlowExpectedUnitProperty] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedProperty",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    port: List[ProductFlowPort] = field(
        default_factory=list,
        metadata={
            "name": "Port",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    relative_coordinate: Optional[RelativeCoordinate] = field(
        default=None,
        metadata={
            "name": "RelativeCoordinate",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
