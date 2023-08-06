from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.deferred_kind import DeferredKind
from prodml22.deferred_production_volume import DeferredProductionVolume
from prodml22.downtime_reason_code import DowntimeReasonCode
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeferredProductionEvent:
    """
    Information about the event or incident that caused production to be
    deferred.

    :ivar start_date: The start date of the event.
    :ivar end_date: The end date of the event.
    :ivar duration: The duration of the event.
    :ivar downtime_reason_code: The reason code for the downtime event.
    :ivar deferred_kind: Indicates whether event is planned or unplanned
    :ivar remark: A brief meaningful description about the event.
    :ivar deferred_production_volume: The production volume deferred for
        the reporting period.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    downtime_reason_code: Optional[DowntimeReasonCode] = field(
        default=None,
        metadata={
            "name": "DowntimeReasonCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    deferred_kind: Optional[DeferredKind] = field(
        default=None,
        metadata={
            "name": "DeferredKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    deferred_production_volume: List[DeferredProductionVolume] = field(
        default_factory=list,
        metadata={
            "name": "DeferredProductionVolume",
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
