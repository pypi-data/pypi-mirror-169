from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DowntimeReasonCode:
    """Codes to categorize the reason for downtime.

    These codes are company specific so they are not part of PRODML.
    Company's can use this schema to specify their downtime codes.

    :ivar name: Name or explanation of the code specified in the code
        attribute.
    :ivar parent:
    :ivar authority: The authority (usually a company) that defines the
        codes.
    :ivar code: The code value.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    parent: Optional["DowntimeReasonCode"] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
