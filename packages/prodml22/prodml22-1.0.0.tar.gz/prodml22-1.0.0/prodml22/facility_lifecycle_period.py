from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.facility_lifecycle_state import FacilityLifecycleState

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FacilityLifecyclePeriod:
    """
    This class is used to represent a period of time when a facility was in a
    lifecycle state.

    :ivar state: The facility's lifecycle state.
    :ivar start_date_time: The date and time when the lifecycle state
        started.
    :ivar end_date_time: The data and time when the lifecycle state
        ended.
    """
    state: Optional[Union[FacilityLifecycleState, str]] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    start_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
