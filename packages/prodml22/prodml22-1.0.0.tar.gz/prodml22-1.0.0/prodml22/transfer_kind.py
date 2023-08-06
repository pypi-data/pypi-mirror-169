from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TransferKind(Enum):
    """
    Specifies if the transfer is input or output.

    :cvar INPUT: Transfer into an asset.
    :cvar OUTPUT: Transfer out of an asset.
    """
    INPUT = "input"
    OUTPUT = "output"
