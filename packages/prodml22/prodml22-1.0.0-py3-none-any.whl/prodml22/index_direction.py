from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class IndexDirection(Enum):
    """Specifies the direction of the index, whether decreasing, increasing or
    unordered.

    For secondary indexes, the direction depends on the direction of the
    primary index. Unordered is only for secondary indexes.

    :cvar DECREASING: For primary indexes, the index value of
        consecutive data points are strictly decreasing. For secondary
        indexes, the index value of consecutive data points are
        monotonically decreasing.
    :cvar INCREASING: For primary indexes, the index value of
        consecutive data points are strictly increasing. For secondary
        indexes, the index value of consecutive data points are
        monotonically increasing.
    :cvar UNORDERED: Not valid for primary indexes. For secondary
        indexes, consecutive index values are not guaranteed to be
        increasing or decreasing.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    UNORDERED = "unordered"
