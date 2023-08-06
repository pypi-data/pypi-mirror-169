from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class GeneralMeasureType:
    """
    General measure type.

    :ivar uom: The unit of measure.
    """
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 32,
        }
    )
