from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class VolumeReferenceKind(Enum):
    """
    Specifies the conditions at which the volume was measured.

    :cvar RESERVOIR:
    :cvar SATURATION_CALCULATED: The reference volume is measured at
        saturation-calculated conditions.
    :cvar SATURATION_MEASURED: The reference volume is measured at
        saturation-measured conditions.
    :cvar SEPARATOR_STAGE_1: The reference volume is measured at
        separator stage 1 conditions.
    :cvar SEPARATOR_STAGE_10: The reference volume is measured at
        separator stage 10 conditions.
    :cvar SEPARATOR_STAGE_2: The reference volume is measured at
        separator stage 2 conditions.
    :cvar SEPARATOR_STAGE_3: The reference volume is measured at
        separator stage 3 conditions.
    :cvar SEPARATOR_STAGE_4: The reference volume is measured at
        separator stage 4 conditions.
    :cvar SEPARATOR_STAGE_5: The reference volume is at measured
        separator stage 5 conditions.
    :cvar SEPARATOR_STAGE_6: The reference volume is measured  at
        separator stage 6 conditions.
    :cvar SEPARATOR_STAGE_7: The reference volume is measured at
        separator stage 7 conditions.
    :cvar SEPARATOR_STAGE_8: The reference volume is measured at
        separator stage 8 conditions.
    :cvar SEPARATOR_STAGE_9: The reference volume is measured at
        separator stage 9 conditions.
    :cvar STOCK_TANK: The reference volume is measured at stock tank
        conditions.
    :cvar TEST_STEP:
    :cvar OTHER:
    """
    RESERVOIR = "reservoir"
    SATURATION_CALCULATED = "saturation-calculated"
    SATURATION_MEASURED = "saturation-measured"
    SEPARATOR_STAGE_1 = "separator stage 1"
    SEPARATOR_STAGE_10 = "separator stage 10"
    SEPARATOR_STAGE_2 = "separator stage 2"
    SEPARATOR_STAGE_3 = "separator stage 3"
    SEPARATOR_STAGE_4 = "separator stage 4"
    SEPARATOR_STAGE_5 = "separator stage 5"
    SEPARATOR_STAGE_6 = "separator stage 6"
    SEPARATOR_STAGE_7 = "separator stage 7"
    SEPARATOR_STAGE_8 = "separator stage 8"
    SEPARATOR_STAGE_9 = "separator stage 9"
    STOCK_TANK = "stock tank"
    TEST_STEP = "test step"
    OTHER = "other"
