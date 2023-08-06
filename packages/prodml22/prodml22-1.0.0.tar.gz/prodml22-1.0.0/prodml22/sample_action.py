from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class SampleAction(Enum):
    """
    Specifies the actions that may be performed to a fluid sample.

    :cvar CUSTODY_TRANSFER: The action on the sample for this event was
        custody transfer to new custodian.
    :cvar DESTROYED: The action on the sample for this event was
        destruction.
    :cvar SAMPLE_TRANSFER: The action on the sample for this event was
        sample transfer.
    :cvar STORED: The action on the sample for this event was movement
        to storage.
    :cvar SUB_SAMPLE_DEAD: The action on the sample for this event was
        sub-sampling under dead conditions.
    :cvar SUB_SAMPLE_LIVE: The action on the sample for this event was
        sub-sampling under live conditions.
    """
    CUSTODY_TRANSFER = "custodyTransfer"
    DESTROYED = "destroyed"
    SAMPLE_TRANSFER = "sampleTransfer"
    STORED = "stored"
    SUB_SAMPLE_DEAD = "subSample Dead"
    SUB_SAMPLE_LIVE = "subSample Live"
