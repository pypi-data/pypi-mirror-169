from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FacilityOperator:
    """
    This class is used to represent the BusinessAssociate that operates or
    operated a facility and, optionally, the time interval during which the
    business associated is or was the operator.

    :ivar business_associate: A pointer to the business associate that
        operates or operated the facility.
    :ivar effective_date_time: The date and time when the business
        associate became the facility operator.
    :ivar termination_date_time: The date and time when the business
        associate ceased to be the facility operator.
    """
    business_associate: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BusinessAssociate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    termination_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminationDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
