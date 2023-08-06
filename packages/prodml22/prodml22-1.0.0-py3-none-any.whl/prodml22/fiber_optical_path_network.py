from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.endpoint_qualified_date_time import EndpointQualifiedDateTime
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.product_flow_external_reference import ProductFlowExternalReference
from prodml22.product_flow_network import ProductFlowNetwork

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOpticalPathNetwork:
    """The sequence of connected items of equipment along the optical path.

    Represented by a flow network.

    :ivar installation: Installation.
    :ivar context_facility: Context facility.
    :ivar dtim_start: DTimStart.
    :ivar dtime_end: DTimeEnd.
    :ivar existence_time: ExistenceTime.
    :ivar dtim_min: DTimMin.
    :ivar dtim_max: DTimMax.
    :ivar comment: Comment.
    :ivar external_connect:
    :ivar network:
    :ivar uid: Unique identifier of this object.
    """
    installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Installation",
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
            "min_occurs": 1,
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
    dtime_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimeEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    existence_time: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "ExistenceTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    dtim_min: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "DTimMin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    dtim_max: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "DTimMax",
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
    external_connect: List[ProductFlowExternalReference] = field(
        default_factory=list,
        metadata={
            "name": "ExternalConnect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    network: List[ProductFlowNetwork] = field(
        default_factory=list,
        metadata={
            "name": "Network",
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
