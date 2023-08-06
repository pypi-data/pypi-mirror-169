from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_date_time_class import AbstractDateTimeType
from prodml22.abstract_object import AbstractObject
from prodml22.calculation_method import CalculationMethod
from prodml22.data_object_reference import DataObjectReference
from prodml22.endpoint_qualified_date_time import EndpointQualifiedDateTime
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.geographic_context import GeographicContext
from prodml22.name_struct import NameStruct
from prodml22.product_volume_business_unit import ProductVolumeBusinessUnit
from prodml22.product_volume_facility import ProductVolumeFacility
from prodml22.reference_condition import ReferenceCondition
from prodml22.reporting_duration_kind import ReportingDurationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolume(AbstractObject):
    """
    The non-contextual content of a product volume object.

    :ivar installation: The name of the facility which is represented by
        this report. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented installation.
    :ivar kind: The type of report.
    :ivar period_kind: The type of period that is being reported. This
        value must be consistent with the reporting start and end
        values.
    :ivar dtim_min: The minimum time index contained within the report.
        For the purposes of this parameter, a "period" or "facility
        parameter" without any time data should be assumed to have the
        time associated with the overall report. The minimum and maximum
        indexes are server query parameters and will be populated with
        valid values in a "get" result.
    :ivar dtim_max: The maximum time index contained within the report.
        For the purposes of this parameter, a "period" or "facility
        parameter" without any time data should be assumed to have the
        time associated with the overall report. The minimum and maximum
        indexes are server query parameters and will be populated with
        valid values in a "get" result.
    :ivar dtim_current: The definition of the "current time" index for
        this report. The current time index is a server query parameter
        which requests the selection of a single node from a recurring
        "period" set (e.g., the data related to one point in a time
        series). For the purposes of this parameter, a "period" without
        any time data should be assumed to have the time associated with
        the overall report.
    :ivar calculation_method: The calculation method for  "filling in"
        values in an indexed set. If not given, the default is that no
        calculations are performed to create data where none exists
        within an existing set. This is not to be construed as to
        prevent concepts such as simulation and forecasting from being
        applied in order to create a new set. This is a server query
        parameter.
    :ivar operator: The operator of the facilities in the report.
    :ivar title: The tile of the report if different from the name of
        the report.
    :ivar geographic_context: The geographic context of the report.
    :ivar issue_date: The date that the report was issued.
    :ivar issued_by: The person or company that issued the report. This
        may contain the role of the person or company within the context
        of the report.
    :ivar approval_date: The date that the report was approved.
    :ivar approver: The person or company that approved the report. This
        may contain the role of the person or company within the context
        of the report.
    :ivar standard_temp_pres: Defines the default standard temperature
        and pressure to which all volumes, densities and flow rates in
        this report have been corrected. The default may be locally
        overridden for an individual value. If not specified, then the
        conditions must be presumed to be ambient conditions (i.e.,
        uncorrected) unless otherwise specified at a local level.
    :ivar facility: A facility for which product information is being
        reported.
    :ivar business_unit: A business unit and related account or
        ownership share information.
    :ivar product_flow_model:
    :ivar date_time:
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
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "max_length": 64,
        }
    )
    period_kind: Optional[ReportingDurationKind] = field(
        default=None,
        metadata={
            "name": "PeriodKind",
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
    dtim_current: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimCurrent",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    calculation_method: Optional[CalculationMethod] = field(
        default=None,
        metadata={
            "name": "CalculationMethod",
            "type": "Element",
        }
    )
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        }
    )
    title: Optional[NameStruct] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        }
    )
    geographic_context: Optional[GeographicContext] = field(
        default=None,
        metadata={
            "name": "GeographicContext",
            "type": "Element",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
        }
    )
    issued_by: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IssuedBy",
            "type": "Element",
        }
    )
    approval_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ApprovalDate",
            "type": "Element",
        }
    )
    approver: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Approver",
            "type": "Element",
        }
    )
    standard_temp_pres: Optional[ReferenceCondition] = field(
        default=None,
        metadata={
            "name": "StandardTempPres",
            "type": "Element",
        }
    )
    facility: List[ProductVolumeFacility] = field(
        default_factory=list,
        metadata={
            "name": "Facility",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    business_unit: List[ProductVolumeBusinessUnit] = field(
        default_factory=list,
        metadata={
            "name": "BusinessUnit",
            "type": "Element",
        }
    )
    product_flow_model: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ProductFlowModel",
            "type": "Element",
        }
    )
    date_time: Optional[AbstractDateTimeType] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
        }
    )
