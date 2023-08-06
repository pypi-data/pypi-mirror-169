from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.endpoint_qualified_date_time import EndpointQualifiedDateTime
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.product_flow_external_reference import ProductFlowExternalReference
from prodml22.product_flow_network import ProductFlowNetwork

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowModel(AbstractObject):
    """
    The non-contextual content of a product flow model data object.

    :ivar installation: The name of the facility that is represented by
        this model. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented installation.
    :ivar dtim_start: The date and time of the start of validity for
        this model.
    :ivar dtim_end: The date and time of the termination of validity for
        this model.
    :ivar existence_time: The time for which "currently existing" data
        is desired from the network. All connections (and related data)
        existing at this time (i.e., start and end bracket this value)
        will  be returned if requested. The existence time is a server
        query parameter.
    :ivar dtim_min: The minimum time index contained within the report.
        The minimum and maximum indexes are server query parameters and
        will be populated with valid values in a "get" result.
    :ivar dtim_max: The maximum time index contained within the report.
        The minimum and maximum indexes are server query parameters and
        will be populated with valid values in a "get" result.
    :ivar comment: A descriptive remark about the model.
    :ivar external_connect: Defines the external port in another Product
        Flow Model to which an external port in this model is connected.
        An external port should be connected to an external port with
        the opposite direction. The connected external port must be in
        another Product Flow Model. These connections should always be
        defined on a one-to-one basis. For example, if a facility may
        receive input from multiple other facilities then a separate
        input port should be defined for each of those facilities. This
        allows any question about mass balancing to be contained within
        each individual model. The external port name must match the
        name of an external port on the network that represents this
        model.
    :ivar network: The description of one named network within this
        model. Each model is self contained but may reference other
        newtorks for defining internal detail. One of the networks must
        represent this model.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Installation",
            "type": "Element",
        }
    )
    context_facility: List[FacilityIdentifierStruct] = field(
        default_factory=list,
        metadata={
            "name": "ContextFacility",
            "type": "Element",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    existence_time: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "ExistenceTime",
            "type": "Element",
        }
    )
    dtim_min: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "DTimMin",
            "type": "Element",
        }
    )
    dtim_max: Optional[EndpointQualifiedDateTime] = field(
        default=None,
        metadata={
            "name": "DTimMax",
            "type": "Element",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    external_connect: List[ProductFlowExternalReference] = field(
        default_factory=list,
        metadata={
            "name": "ExternalConnect",
            "type": "Element",
        }
    )
    network: List[ProductFlowNetwork] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "min_occurs": 1,
        }
    )
