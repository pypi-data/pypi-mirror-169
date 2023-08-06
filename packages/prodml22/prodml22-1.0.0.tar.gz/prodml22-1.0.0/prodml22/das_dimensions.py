from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DasDimensions(Enum):
    """Specifies the possible orientations of the data array. For multiple H5
    files:

    - Must specify that the indexes split OVER TIME
    - Even if loci were the index
    - Each divided file still contains the split time array

    :cvar FREQUENCY: Enumeration value to indicate the frequency
        dimension in a multi-dimensional array.
    :cvar LOCUS: Enumeration value to indicate the locus dimension in a
        multi-dimensional array.
    :cvar TIME: Enumeration value to indicate the time dimension in a
        multi-dimensional array.
    """
    FREQUENCY = "frequency"
    LOCUS = "locus"
    TIME = "time"
