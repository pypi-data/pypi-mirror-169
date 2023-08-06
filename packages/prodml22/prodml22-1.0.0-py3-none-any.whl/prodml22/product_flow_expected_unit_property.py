from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.expected_flow_qualifier import ExpectedFlowQualifier
from prodml22.facility_parameter import FacilityParameter
from prodml22.general_measure_type import GeneralMeasureType
from prodml22.name_struct import NameStruct
from prodml22.product_flow_qualifier_expected import ProductFlowQualifierExpected
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFlowExpectedUnitProperty:
    """
    Defines expected properties of a facility represented by a unit.

    :ivar property: The expected kind of facility property. Each
        property is documented to have values of a particular type.
    :ivar child_facility_identifier: The PRODML Relative Identifier (or
        URI) of a child of the parent facility. The identifier path is
        presumed to begin with the identity of the parent facility. This
        identifies a sub-facility which is identified within the context
        of the parent facilityParent2/facilityParent1/name
        identification hierarchy. The property is only expected to be
        defined for this child and not for the parent. For more
        information about URIs, see the Energistics Identifier
        Specification, which is available in the zip file when download
        PRODML.
    :ivar tag_alias: An alternative name for the sensor that  measures
        the property.
    :ivar deadband: Difference between two consecutive readings, which
        must exceed deadband value to be accepted.
    :ivar maximum_frequency: The maximum time difference from the last
        sent event before the next event is sent.
    :ivar comment: A descriptive remark associated with this property.
    :ivar expected_flow_qualifier: Forces a choice between a qualifier
        or one more qualified by flow and product.
    :ivar expected_flow_product: Defines the expected flow and product
        pairs to be assigned to this port by a Product Volume report. A
        set of expected qualifiers can be defined for each pair. The
        aggregate of expectations on all properties should be a subset
        of the aggregate of expectations on the port. If no expectations
        are defined on the port then the port aggregate will be defined
        by the properties.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    property: Optional[FacilityParameter] = field(
        default=None,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    child_facility_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChildFacilityIdentifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tag_alias: List[NameStruct] = field(
        default_factory=list,
        metadata={
            "name": "TagAlias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    deadband: Optional[GeneralMeasureType] = field(
        default=None,
        metadata={
            "name": "Deadband",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    maximum_frequency: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumFrequency",
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
    expected_flow_qualifier: Optional[ExpectedFlowQualifier] = field(
        default=None,
        metadata={
            "name": "ExpectedFlowQualifier",
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
