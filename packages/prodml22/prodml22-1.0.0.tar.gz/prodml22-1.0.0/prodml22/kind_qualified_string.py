from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_measure_data import AbstractMeasureData
from prodml22.value_status import ValueStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class KindQualifiedString(AbstractMeasureData):
    """A kind which may have a quality status.

    If the 'status' attribute is absent and the value is not "NaN", the
    data value can be assumed to be good with no restrictions.

    :ivar status: An indicator of the quality of the value.
    """
    status: Optional[ValueStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
