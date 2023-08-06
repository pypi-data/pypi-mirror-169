from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.balance_destination_type import BalanceDestinationType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeDestination:
    """
    Product Flow Sales Destination Schema.

    :ivar name: The name of the destination.
    :ivar type: The type of destination.
    :ivar country: The country of the destination.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    type: Optional[BalanceDestinationType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
