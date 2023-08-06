from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractModelSection:
    """
    The abstract class of model section that forces a choice between a wellbore
    base or a reservoir base.

    :ivar comment: The method used for this section of the results. Text
        description. No semantic meaning.
    :ivar method: The method used for this section of the results. Text
        description. No semantic meaning.
    """
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    method: Optional[str] = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
