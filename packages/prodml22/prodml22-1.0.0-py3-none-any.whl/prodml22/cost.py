from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Cost:
    """
    The price of an item, with a currency indication.

    :ivar value:
    :ivar currency: Currency used for this Cost. Use of ISO 4217
        alphabetic codes for transfers would be a best practice.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
