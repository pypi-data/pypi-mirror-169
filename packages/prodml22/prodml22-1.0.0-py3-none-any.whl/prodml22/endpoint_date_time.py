from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.endpoint_qualifier_interval import EndpointQualifierInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class EndpointDateTime:
    """A value used for the endpoint of a date-time interval.

    The meaning of the endpoint of an interval must be defined by the
    endpoint attribute.

    :ivar value:
    :ivar endpoint: Defines the semantics (inclusive or exclusive) of
        the endpoint within the context of the interval.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    endpoint: Optional[EndpointQualifierInterval] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
