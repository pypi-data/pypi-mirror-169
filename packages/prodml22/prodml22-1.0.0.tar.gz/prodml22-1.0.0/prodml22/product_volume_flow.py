from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.common_properties_product_volume import CommonPropertiesProductVolume
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.flow_qualifier import FlowQualifier
from prodml22.flow_sub_qualifier import FlowSubQualifier
from prodml22.name_struct import NameStruct
from prodml22.product_flow_port_type import ProductFlowPortType
from prodml22.product_volume_product import ProductVolumeProduct
from prodml22.product_volume_related_facility import ProductVolumeRelatedFacility
from prodml22.reporting_flow import ReportingFlow

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeFlow:
    """
    Product Volume Flow Component Schema.

    :ivar name: The name of this flow within the context of this report.
        This might reflect some combination of the kind of flow, port,
        qualifier and related facility.
    :ivar kind: Indicates the type of flow that is being reported. The
        type of flow is an indication of the overall source or target of
        the flow.  - A production flow has one or more wells as the
        originating source.  - An injection flow has one or more wells
        as the ultimate target.  - An import flow has an offsite source.
        - An export flow has an offsite target. - A consumption flow
        generally has a kind of equipment as a target.
    :ivar port: Port.
    :ivar direction: Direction.
    :ivar facility: Facility.
    :ivar facility_alias: Facility alias.
    :ivar qualifier: Qualifies the type of flow that is being reported.
    :ivar sub_qualifier: Defines a specialization of the qualifier
        value. This should only be given if a qualifier is given.
    :ivar version: Version.
    :ivar version_source: Identifies the source of the version. This
        will commonly be the name of the software which created the
        version.
    :ivar source_flow: This is a pointer to the flow from which this
        flow was derived.
    :ivar related_facility:
    :ivar product: Reports a product flow stream.
    :ivar properties:
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
    kind: Optional[ReportingFlow] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    port: Optional[str] = field(
        default=None,
        metadata={
            "name": "Port",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    direction: Optional[ProductFlowPortType] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    qualifier: Optional[FlowQualifier] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sub_qualifier: Optional[FlowSubQualifier] = field(
        default=None,
        metadata={
            "name": "SubQualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    version_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionSource",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    source_flow: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceFlow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    related_facility: Optional[ProductVolumeRelatedFacility] = field(
        default=None,
        metadata={
            "name": "RelatedFacility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    product: List[ProductVolumeProduct] = field(
        default_factory=list,
        metadata={
            "name": "Product",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    properties: Optional[CommonPropertiesProductVolume] = field(
        default=None,
        metadata={
            "name": "Properties",
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
