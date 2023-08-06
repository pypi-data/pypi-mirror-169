from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dts_interpretation_data import DtsInterpretationData

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsInterpretationLogSet:
    """
    Container of interpreted data which also specifies by reference the
    measured data on which the interpretation is based.

    :ivar preferred_interpretation_reference: For a set of
        dtsInterpretedData logs that are generated from the same
        measurement (each log having gone through a different post-
        processing type, for example), if there is one log that is
        ‘preferred’ for additional business decisions (while the other
        ones were merely what-if scenarios), then this preferred log in
        the collection of child dtsInterpretedData can be flagged by
        referencing its UID with this element.
    :ivar interpretation_data:
    """
    preferred_interpretation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferredInterpretationReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    interpretation_data: List[DtsInterpretationData] = field(
        default_factory=list,
        metadata={
            "name": "InterpretationData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
