from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.facility_identifier_struct import FacilityIdentifierStruct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowExternalReference:
    """
    A reference to an external port in a different product flow model.This
    value represents a foreign key from one element to another.

    :ivar port_reference: Reference to a type of port.
    :ivar connected_port_reference: Reference to the connected port.
    :ivar connected_model_reference: Reference to the connected model.
    :ivar connected_installation:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top level object.
    """
    port_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    connected_port_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectedPortReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    connected_model_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectedModelReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    connected_installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "ConnectedInstallation",
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
