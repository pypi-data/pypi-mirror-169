from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class IlluminanceUom(Enum):
    """
    :cvar FOOTCANDLE: footcandle
    :cvar KLX: kilolux
    :cvar LM_M2: lumen per square metre
    :cvar LX: lux
    """
    FOOTCANDLE = "footcandle"
    KLX = "klx"
    LM_M2 = "lm/m2"
    LX = "lx"
