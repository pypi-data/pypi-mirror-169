from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.column import Column

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class NestedColumnBasedTable:
    """
    Allows a table to be contained in an abstract object (AbstractObject)
    without carrying all of the information of an abstract object (such as
    UUID, schema version, object version, aliases, extensions, etc.) Also, it
    is not a data object, meaning it is not discoverable by itself in an ETP
    context.
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 256,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    key_column: List[Column] = field(
        default_factory=list,
        metadata={
            "name": "KeyColumn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    column: List[Column] = field(
        default_factory=list,
        metadata={
            "name": "Column",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
