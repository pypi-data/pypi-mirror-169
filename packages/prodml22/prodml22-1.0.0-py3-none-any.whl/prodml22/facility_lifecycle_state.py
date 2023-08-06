from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class FacilityLifecycleState(Enum):
    """
    :cvar PLANNING: All the activities of the Life Cycle before
        construction has commenced. It includes designing a well [or
        other facility] and obtaining management and regulatory
        approvals.
    :cvar CONSTRUCTING: The approved activities of the Life Cycle prior
        to operation.
    :cvar OPERATING: The activities of the Life Cycle while the well [or
        facility] is capable of performing its intended Role. It
        includes periods where it is temporarily shut in [not active.]
    :cvar CLOSING: The set of activities of the Life Cycle to make the
        well or [other facility] permanently incapable of any Role.
    :cvar CLOSED: The phase of the Life Cycle when the well [or
        facility] is permanently incapable of performing any Role.
    """
    PLANNING = "planning"
    CONSTRUCTING = "constructing"
    OPERATING = "operating"
    CLOSING = "closing"
    CLOSED = "closed"
