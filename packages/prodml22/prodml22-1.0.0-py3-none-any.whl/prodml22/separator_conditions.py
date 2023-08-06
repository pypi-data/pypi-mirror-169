from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SeparatorConditions:
    """
    Separator conditions.

    :ivar separator_test_reference: Reference to a separator test
        element, which contains the separator conditions (stages) which
        apply to this test.
    """
    separator_test_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "separatorTestReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
