from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.quantity_method import QuantityMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Injection:
    """
    Volume injected per reporting entity.

    :ivar quantity_method: The method in which the quantity/volume was
        determined. See enum QuantityMethod.
    :ivar remark: A descriptive remark relating to any significant
        events.
    :ivar injection_quantity:
    """
    quantity_method: Optional[Union[QuantityMethod, str]] = field(
        default=None,
        metadata={
            "name": "QuantityMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    injection_quantity: List[AbstractProductQuantity] = field(
        default_factory=list,
        metadata={
            "name": "InjectionQuantity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
