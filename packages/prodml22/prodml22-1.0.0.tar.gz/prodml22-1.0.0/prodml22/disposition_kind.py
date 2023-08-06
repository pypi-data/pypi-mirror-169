from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DispositionKind(Enum):
    """
    Specifies the set of categories used to account for how crude oil and
    petroleum products are transferred, distributed, or removed from the supply
    stream (e.g.,stock change, crude oil losses, exports, sales, etc.).

    :cvar BUYBACK: Buyback is the purchase/transfer of hydrocarbon from
        off-lease facilities to the lease for the purpose of using it in
        the lease for operation purposes.
    :cvar FLARED: Burned in a flare.
    :cvar SOLD: Sold and transported to a buyer by pipeline.
    :cvar USED_ON_SITE: Used for entity operations.
    :cvar FUEL: Consumed by processing equipment.
    :cvar VENTED: Released into the atmosphere.
    :cvar DISPOSAL: Disposed of.
    :cvar GAS_LIFT: Injected into a producing well for artificial lift.
    :cvar LOST_OR_STOLEN: Lost or stolen.
    :cvar OTHER: Physically removed from the entity location.
    """
    BUYBACK = "buyback"
    FLARED = "flared"
    SOLD = "sold"
    USED_ON_SITE = "used on-site"
    FUEL = "fuel"
    VENTED = "vented"
    DISPOSAL = "disposal"
    GAS_LIFT = "gas lift"
    LOST_OR_STOLEN = "lost or stolen"
    OTHER = "other"
