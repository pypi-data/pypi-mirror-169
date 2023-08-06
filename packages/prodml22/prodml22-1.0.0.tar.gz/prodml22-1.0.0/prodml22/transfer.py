from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_simple_product_volume import AbstractSimpleProductVolume
from prodml22.data_object_reference import DataObjectReference
from prodml22.product_fluid import ProductFluid
from prodml22.transfer_kind import TransferKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Transfer(AbstractSimpleProductVolume):
    """Information about products transferred across asset group boundaries or
    leaving the jurisdiction of an operator.

    This may include pipeline exports, output to refineries, etc.

    :ivar transfer_kind: Specifies the kind of transfer. See enum
        TransferKind.
    :ivar start_time: The date and time when the transfer began.
    :ivar end_time: Date and time when the transfer ended.
    :ivar destination_facility:
    :ivar source_facility:
    :ivar product_transfer_quantity: The amount of product transferred.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    transfer_kind: Optional[TransferKind] = field(
        default=None,
        metadata={
            "name": "TransferKind",
            "type": "Element",
            "required": True,
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
    destination_facility: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DestinationFacility",
            "type": "Element",
            "required": True,
        }
    )
    source_facility: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SourceFacility",
            "type": "Element",
            "required": True,
        }
    )
    product_transfer_quantity: List[ProductFluid] = field(
        default_factory=list,
        metadata={
            "name": "ProductTransferQuantity",
            "type": "Element",
        }
    )
