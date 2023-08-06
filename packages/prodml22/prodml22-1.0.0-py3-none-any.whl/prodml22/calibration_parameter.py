from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CalibrationParameter:
    """Parameters are given by name/ value pairs, with optional UOM.

    The parameter name and UOM are attributes, and the value is the
    value of the element.

    :ivar uom: The unit of measure of the parameter value.
    :ivar name: The name of the parameter.
    """
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 32,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
