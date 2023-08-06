from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PlusComponentKind(Enum):
    """
    Specifies the types of plus components.
    """
    C10 = "c10+"
    C11 = "c11+"
    C12 = "c12+"
    C20 = "c20+"
    C25 = "c25+"
    C30 = "c30+"
    C36 = "c36+"
    C5 = "c5+"
    C6 = "c6+"
    C7 = "c7+"
    C8 = "c8+"
    C9 = "c9+"
