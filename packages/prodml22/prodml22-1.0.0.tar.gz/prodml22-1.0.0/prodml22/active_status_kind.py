from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ActiveStatusKind(Enum):
    """
    Specifies the active status of the object: active or inactive.

    :cvar ACTIVE: Currently active. For channels and growing objects,
        data or parts are being added, updated or deleted. For other
        objects, channels or growing objects associated with them are
        active.
    :cvar INACTIVE: Currently inactive. For channels and growing
        objects, no data or parts have been recently added, updated or
        deleted. For other objects, no channels or growing objects
        associated with them are currently active.
    """
    ACTIVE = "active"
    INACTIVE = "inactive"
