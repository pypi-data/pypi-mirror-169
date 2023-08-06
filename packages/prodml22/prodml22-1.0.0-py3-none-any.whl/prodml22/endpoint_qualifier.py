from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class EndpointQualifier(Enum):
    """
    Specifies values for the endpoint for min/max query parameters on "growing
    objects".

    :cvar EXCLUSIVE: The value is excluded.
    :cvar EXTENSIVE: The endpoint of the range may be extended to the
        first encountered value if an exact value match is not
        found.That is, if a node index value does not match the
        specified range value then the next smaller value (on minimum
        end) or larger value (on maximum end) in the index series should
        be used as the endpoint. Basically, this concept is designed to
        support interpolation across an undefined point.
    :cvar INCLUSIVE: The value is included.
    :cvar OVERLAP_EXTENSIVE: The endpoint of the range may be extended
        to the first encountered value if the interval is overlapped
        with the index interval. That is, if a node index value does not
        match the specified range value then the next smaller value (on
        minimum end) or larger value (on maximum end) in the index
        series should be used as the endpoint. This concept is designed
        to select ALL nodes whose index interval overlap with the query
        range.
    """
    EXCLUSIVE = "exclusive"
    EXTENSIVE = "extensive"
    INCLUSIVE = "inclusive"
    OVERLAP_EXTENSIVE = "overlap extensive"
