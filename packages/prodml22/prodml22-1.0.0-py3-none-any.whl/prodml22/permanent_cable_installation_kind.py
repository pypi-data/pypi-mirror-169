from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PermanentCableInstallationKind(Enum):
    """
    Specifies the types of permanent cable installations.
    """
    BURIED_PARALLEL_TO_TUBULAR = "buried parallel to tubular"
    CLAMPED_TO_TUBULAR = "clamped to tubular"
    WRAPPED_AROUND_TUBULAR = "wrapped around tubular"
