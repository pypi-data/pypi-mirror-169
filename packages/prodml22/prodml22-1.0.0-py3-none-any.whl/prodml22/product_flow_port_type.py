from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ProductFlowPortType(Enum):
    """
    Specifies the types of product flow ports.
    """
    INLET = "inlet"
    OUTLET = "outlet"
    UNKNOWN = "unknown"
