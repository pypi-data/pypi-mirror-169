from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.authority_qualified_name import AuthorityQualifiedName
from prodml22.quantity_method import QuantityMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractDisposition:
    """
    The Abstract base type of disposition.

    :ivar quantity_method: Quantity method.
    :ivar product_disposition_code: A unique disposition code associated
        within a given naming system. This may be a code specified by a
        regulatory agency.
    :ivar remark: A descriptive remark relating to this disposition.
    :ivar disposition_quantity: The amount of product to which this
        disposition applies.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
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
    product_disposition_code: Optional[AuthorityQualifiedName] = field(
        default=None,
        metadata={
            "name": "ProductDispositionCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    disposition_quantity: List[AbstractProductQuantity] = field(
        default_factory=list,
        metadata={
            "name": "DispositionQuantity",
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
