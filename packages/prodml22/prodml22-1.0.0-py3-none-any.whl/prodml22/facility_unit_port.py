from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_related_facility_object import AbstractRelatedFacilityObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FacilityUnitPort(AbstractRelatedFacilityObject):
    """
    Facility unit port.

    :ivar port_reference: The product flow port associated with the
        product flow unit.
    :ivar unit_reference: The product flow unit representing the
        facility.
    :ivar network_reference: The product flow network representing the
        facility. This is only required if the network is not the same
        as the primary network that represents the Product Flow Model.
        This must be unique within the context of the product flow model
        represented by this report.
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
    unit_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    network_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetworkReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
