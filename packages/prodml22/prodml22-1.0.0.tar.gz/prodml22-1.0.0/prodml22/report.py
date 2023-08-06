from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.geographic_context import GeographicContext
from prodml22.report_version_status import ReportVersionStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Report(AbstractObject):
    """
    Report.

    :ivar kind: The type of report. This should define and constrain the
        expected content of the report.
    :ivar date: The date that the report represents (i.e., not a year or
        month). Only one of date, month or year should be specified.
    :ivar date_end: The ending date that the report represents, if it
        represents an interval.
    :ivar month: The month that the report represents (i.e., not a year,
        date or date range). Only one of date, month or year should be
        specified.
    :ivar year: The year that the report represents (i.e., not a month,
        date or date range). Only one of date, month or year should be
        specified.
    :ivar comment: A textual comment about the report.
    :ivar report_version: The current report version.
    :ivar report_status: The current document version status.
    :ivar installation: The name of the facility which is represented by
        this report. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented installation.
    :ivar issue_date: The date that the report was issued.
    :ivar approval_date: The date that the report was approved.
    :ivar operator:
    :ivar issued_by:
    :ivar approver:
    :ivar geographic_context: A geographic context of a report.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "max_length": 64,
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
        }
    )
    date_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateEnd",
            "type": "Element",
        }
    )
    month: Optional[str] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
            "max_length": 64,
            "pattern": r"([1-9][0-9][0-9][0-9])-(([0][0-9])|([1][0-2]))",
        }
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "min_inclusive": 1000,
            "max_inclusive": 9999,
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
    report_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportVersion",
            "type": "Element",
            "max_length": 64,
        }
    )
    report_status: Optional[ReportVersionStatus] = field(
        default=None,
        metadata={
            "name": "ReportStatus",
            "type": "Element",
        }
    )
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
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
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
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
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
    geographic_context: Optional[GeographicContext] = field(
        default=None,
        metadata={
            "name": "GeographicContext",
            "type": "Element",
        }
    )
