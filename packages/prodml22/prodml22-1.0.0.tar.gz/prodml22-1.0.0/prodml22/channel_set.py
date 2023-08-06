from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_object import AbstractObject
from prodml22.channel import Channel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ChannelSet(AbstractObject):
    """A grouping of channels with a compatible index, for some purpose.

    Each channel has its own index. A ‘compatible’ index simply means
    that all of the channels are either in time or in depth using a
    common datum.

    :ivar data: The data blob in JSON form. This attribute lets you
        embed the bulk data in a single file with the xml, to avoid the
        issues that arise when splitting data across multiple files.
        BUSINESS RULE: Either this element or the FileUri element must
        be present.
    :ivar channel:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    data: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Data",
            "type": "Element",
        }
    )
    channel: List[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
        }
    )
