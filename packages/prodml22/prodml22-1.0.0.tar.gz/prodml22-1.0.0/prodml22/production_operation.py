from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_date_time_class import AbstractDateTimeType
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.geographic_context import GeographicContext
from prodml22.name_struct import NameStruct
from prodml22.production_operation_installation_report import ProductionOperationInstallationReport
from prodml22.reporting_duration_kind import ReportingDurationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperation(AbstractObject):
    """
    The non-contextual content of a Production Operation object.

    :ivar installation: The name of the facility which is represented by
        this report. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented installation.
    :ivar kind: The type of report.
    :ivar period_kind: The type of period that is being reported. This
        value must be consistent with the reporting start and end
        values.
    :ivar issue_date: The date that the report was issued.
    :ivar title: The title of the report, if different from the name of
        the report.
    :ivar approval_date: The date that the report was approved.
    :ivar installation_report: A report for each installation
    :ivar issued_by:
    :ivar approver:
    :ivar operator:
    :ivar geographic_context: The geographic context of the report.
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
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
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
    approval_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ApprovalDate",
            "type": "Element",
        }
    )
    installation_report: List[ProductionOperationInstallationReport] = field(
        default_factory=list,
        metadata={
            "name": "InstallationReport",
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
    approver: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Approver",
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
    geographic_context: Optional[GeographicContext] = field(
        default=None,
        metadata={
            "name": "GeographicContext",
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
