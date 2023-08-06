from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AddressQualifier(Enum):
    """
    Specifies qualifiers that can be used for addresses or phone numbers.

    :cvar PERMANENT: permanent
    :cvar PERSONAL: personal
    :cvar WORK:
    """
    PERMANENT = "permanent"
    PERSONAL = "personal"
    WORK = "work"
