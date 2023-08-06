from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeAlert:
    """
    Alert Schema.

    :ivar target: An XPATH to the target value within the message
        containing this XPATH value.
    :ivar level: The level of the alert.
    :ivar type: The type of alert. For example "off specification".
    :ivar description: A textual description of the alert.
    """
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
