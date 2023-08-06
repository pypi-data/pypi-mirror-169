from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.estimation_method import EstimationMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeferredProductionVolume:
    """
    The production volume deferred for the reporting period.

    :ivar estimation_method: The method used to estimate deferred
        production. See enum EstimationMethod.
    :ivar remark: Remarks and comments about this data item.
    :ivar deferred_product_quantity:
    """
    estimation_method: Optional[Union[EstimationMethod, str]] = field(
        default=None,
        metadata={
            "name": "EstimationMethod",
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
    deferred_product_quantity: Optional[AbstractProductQuantity] = field(
        default=None,
        metadata={
            "name": "DeferredProductQuantity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
