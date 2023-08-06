from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.business_unit_kind import BusinessUnitKind
from prodml22.product_volume_business_sub_unit import ProductVolumeBusinessSubUnit

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeBusinessUnit:
    """
    Product volume schema for defining business units.

    :ivar kind: The type of business unit.
    :ivar name: The human contextual name of the business unit.
    :ivar description: A textual description of the business unit.
    :ivar sub_unit: A component part of the unit. The composition of a
        unit may vary with time. This defines the ownership share or
        account information for a sub unit within the context of the
        whole unit. For ownership shares, at any one point in time the
        sum of the shares should be 100%.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[BusinessUnitKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
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
    sub_unit: List[ProductVolumeBusinessSubUnit] = field(
        default_factory=list,
        metadata={
            "name": "SubUnit",
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
