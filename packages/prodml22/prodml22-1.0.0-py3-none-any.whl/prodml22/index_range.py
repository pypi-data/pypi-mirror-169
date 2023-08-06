from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IndexRange:
    """In the case that the ReferencedData is indexed and the conformance with
    the DataAssurance policy applies to a range within that index space, this
    class represents that range.

    The elements are string types because the index could be of numerous
    data types, including integer, float and date.

    :ivar index_minimum: The minimum index for the range over which the
        referenced data's conformance with the policy is being assessed.
    :ivar index_maximum: The maximum index for the range over which the
        referenced data's conformance with the policy is being assessed.
    """
    index_minimum: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexMinimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    index_maximum: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexMaximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
