from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class Otdrreason(Enum):
    """
    Specifies the reasons an OTDR test was run within a distributed temperature
    survey (DTS).

    :cvar DTS: dts
    :cvar OTHER: other
    :cvar POST_INSTALLATION: post-installation
    :cvar PRE_INSTALLATION: pre-installation
    :cvar RUN: run
    """
    DTS = "dts"
    OTHER = "other"
    POST_INSTALLATION = "post-installation"
    PRE_INSTALLATION = "pre-installation"
    RUN = "run"
