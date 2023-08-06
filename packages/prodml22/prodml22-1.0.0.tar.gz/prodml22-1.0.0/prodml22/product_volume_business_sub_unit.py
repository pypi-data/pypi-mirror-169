from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.ownership_business_acct import OwnershipBusinessAcct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeBusinessSubUnit:
    """
    Product volume schema for defining ownership shares of business units.

    :ivar kind: Points to business unit which is part of another
        business unit.
    :ivar ownership_business_acct: Owner business account
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    ownership_business_acct: Optional[OwnershipBusinessAcct] = field(
        default=None,
        metadata={
            "name": "OwnershipBusinessAcct",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
