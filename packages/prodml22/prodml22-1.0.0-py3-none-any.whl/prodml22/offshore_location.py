from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.north_sea_offshore import NorthSeaOffshore

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OffshoreLocation:
    """A generic type of offshore location.

    This allows an offshore location to be given by an area name, and up
    to four block names. A comment is also allowed.

    :ivar area_name: A general meaning of area. It may be as general as
        'UK North Sea' or 'Viosca Knoll'. The user community must agree
        on the meaning of this element.
    :ivar block_id: A block ID that can more tightly locate the object.
        The BlockID should be an identifying name or code. The user
        community for an area must agree on the exact meaning of this
        element. An aggregate of increasingly specialized block IDs are
        sometimes necessary to define the location.
    :ivar comment: An general comment that further explains the offshore
        location.
    :ivar north_sea_offshore: A type of offshore location that captures
        the North Sea offshore terminology.
    """
    area_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    block_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BlockID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    north_sea_offshore: Optional[NorthSeaOffshore] = field(
        default=None,
        metadata={
            "name": "NorthSeaOffshore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
