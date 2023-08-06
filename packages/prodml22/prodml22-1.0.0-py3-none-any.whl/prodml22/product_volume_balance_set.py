from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.balance_flow_part import BalanceFlowPart
from prodml22.product_volume_balance_detail import ProductVolumeBalanceDetail
from prodml22.product_volume_destination import ProductVolumeDestination

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeBalanceSet:
    """
    Product Flow Balance Set Schema.

    :ivar kind: Defines the aspect being described.
    :ivar cargo_number: A cargo identifier for the product.
    :ivar cargo_batch_number: A cargo batch number. Used if the vessel
        needs to temporarily disconnect for some reason (e.g., weather).
    :ivar shipper: The name of the shipper
    :ivar balance_detail:
    :ivar destination:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[BalanceFlowPart] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cargo_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CargoNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cargo_batch_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "CargoBatchNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    shipper: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shipper",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    balance_detail: List[ProductVolumeBalanceDetail] = field(
        default_factory=list,
        metadata={
            "name": "BalanceDetail",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    destination: Optional[ProductVolumeDestination] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
