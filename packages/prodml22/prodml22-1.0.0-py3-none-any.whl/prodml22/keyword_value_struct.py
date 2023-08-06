from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.time_series_keyword import TimeSeriesKeyword

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class KeywordValueStruct:
    """A value for the specified keyword.

    That is, a keyword-value pair. The allowed length of the value is
    constrained by the keyword.

    :ivar value:
    :ivar keyword: The keyword within which the value is unique. The
        concept of a keyword is very close to the concept of a
        classification system.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    keyword: Optional[TimeSeriesKeyword] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
