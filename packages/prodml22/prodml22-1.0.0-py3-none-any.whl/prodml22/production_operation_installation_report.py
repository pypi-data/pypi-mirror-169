from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.crew_count import CrewCount
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.production_operation_activity import ProductionOperationActivity
from prodml22.production_operation_hse import ProductionOperationHse
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationInstallationReport:
    """
    Installation Report Schema.

    :ivar installation: The installation represented by this report.
    :ivar beds_available: Total count of beds available on the
        installation.
    :ivar work: The total cumulative amount of time worked during the
        reporting period. Commonly specified in units of hours. Note
        that a day unit translates to 24 hours worked.
    :ivar work_month_to_date: The total cumulative amount of time worked
        from the beginning of the month to the end of reporting period.
        Commonly specified in units of hours. Note that a day unit
        translates to 24 hours worked.
    :ivar work_year_to_date: The total cumulative amount of time worked
        from the beginning of the year to the end of reporting period.
        Commonly specified in units of hours. Note that a day unit
        translates to 24 hours worked.
    :ivar crew_count: A one-based count of personnel on a type of crew.
    :ivar production_activity: Production activities.
    :ivar operational_hse: Health, Safety and Environmenal information.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Installation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    beds_available: Optional[int] = field(
        default=None,
        metadata={
            "name": "BedsAvailable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    work: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Work",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    work_month_to_date: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "WorkMonthToDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    work_year_to_date: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "WorkYearToDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    crew_count: List[CrewCount] = field(
        default_factory=list,
        metadata={
            "name": "CrewCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    production_activity: Optional[ProductionOperationActivity] = field(
        default=None,
        metadata={
            "name": "ProductionActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    operational_hse: List[ProductionOperationHse] = field(
        default_factory=list,
        metadata={
            "name": "OperationalHSE",
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
