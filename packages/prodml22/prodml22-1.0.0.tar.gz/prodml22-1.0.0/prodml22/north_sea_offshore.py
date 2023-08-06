from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NorthSeaOffshore:
    """
    A type of offshore location that captures the North Sea offshore
    terminology.

    :ivar area_name: An optional, uncontrolled value, which may be used
        to describe the general area of offshore North Sea in which the
        point is located.
    :ivar quadrant: The number or letter of the quadrant in the North
        Sea.
    :ivar block_suffix: A lower case letter assigned if a block is
        subdivided.
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
    quadrant: Optional[str] = field(
        default=None,
        metadata={
            "name": "Quadrant",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    block_suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlockSuffix",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
