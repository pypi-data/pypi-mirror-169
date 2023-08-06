from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_simple_product_volume import AbstractSimpleProductVolume
from prodml22.data_object_reference import DataObjectReference
from prodml22.product_fluid import ProductFluid

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TerminalLifting(AbstractSimpleProductVolume):
    """
    Summarizes product import to or export from an asset by ship.

    :ivar certificate_number: The certificate number for the document
        that defines the lifting onto the tanker.
    :ivar start_time: The date and time when the lifting began.
    :ivar end_time: The date and time when the lifting ended.
    :ivar tanker:
    :ivar destination_terminal:
    :ivar loading_terminal:
    :ivar product_quantity: The amount of product lifted.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    certificate_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateNumber",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    tanker: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tanker",
            "type": "Element",
            "required": True,
        }
    )
    destination_terminal: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DestinationTerminal",
            "type": "Element",
        }
    )
    loading_terminal: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LoadingTerminal",
            "type": "Element",
            "required": True,
        }
    )
    product_quantity: List[ProductFluid] = field(
        default_factory=list,
        metadata={
            "name": "ProductQuantity",
            "type": "Element",
        }
    )
