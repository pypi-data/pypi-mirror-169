from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.curve_definition import CurveDefinition
from prodml22.facility_parameter import FacilityParameter
from prodml22.flow_qualifier import FlowQualifier
from prodml22.flow_sub_qualifier import FlowSubQualifier
from prodml22.measure_class import MeasureType
from prodml22.product_volume_parameter_value import ProductVolumeParameterValue
from prodml22.reporting_duration_kind import ReportingDurationKind
from prodml22.reporting_product import ReportingProduct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeParameterSet:
    """
    Product Volume Facility Parameter Set Schema.

    :ivar name: The name of the facility parameter. This should reflect
        the business semantics of all values in the set and not the
        underlying kind. For example, specify "diameter" rather than
        "length" or "distance".
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
    :ivar port: The port to which this parameter is assigned. This must
        be a port on the unit representing the parent facility of this
        parameter. If not specified then the parameter represents the
        unit.
    :ivar measure_class: If the value is a measure (value with unit of
        measure), this defines the measurement class of the value. The
        units of measure for the value must conform to the list allowed
        by the measurement class in the unit dictionary file. Mutually
        exclusive with curveDefinition.
    :ivar coordinate_reference_system: The pointer to the coordinate
        reference system (CRS). This is needed for coordinates such as
        measured depth to specify the reference datum.
    :ivar qualifier: Qualifies the type of parameter that is being
        reported.
    :ivar sub_qualifier: Defines a specialization of the qualifier
        value. This should only be given if a qualifier is given.
    :ivar version: A timestamp representing the version of this data. A
        parameter set with a more recent timestamp will represent the
        "current" version.
    :ivar version_source: Identifies the source of the version. This
        will commonly be the name of the software which created the
        version.
    :ivar product: The type of product that is being reported. This
        would be useful for something like specifying a tank product
        volume or level.
    :ivar period_kind: The type of period that is being reported.
    :ivar comment: A comment about the parameter.
    :ivar parameter: A parameter value, possibly at a time. If a time is
        not given then only one parameter should be given. If a time is
        specified with one value then time should be specified for all
        values. Each value in a time series should be of the same
        underling kind of value (for example, a length measure).
    :ivar curve_definition: If the value is a curve, this defines the
        meaning of the one column in the table representing the curve.
        Mutually exclusive with measureClass.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    name: Optional[FacilityParameter] = field(
        default=None,
        metadata={
            "name": "Name",
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
    port: Optional[str] = field(
        default=None,
        metadata={
            "name": "Port",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    coordinate_reference_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinateReferenceSystem",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    product: Optional[ReportingProduct] = field(
        default=None,
        metadata={
            "name": "Product",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    period_kind: Optional[ReportingDurationKind] = field(
        default=None,
        metadata={
            "name": "PeriodKind",
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
    parameter: List[ProductVolumeParameterValue] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    curve_definition: List[CurveDefinition] = field(
        default_factory=list,
        metadata={
            "name": "CurveDefinition",
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
