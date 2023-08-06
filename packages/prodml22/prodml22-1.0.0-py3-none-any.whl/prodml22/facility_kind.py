from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FacilityKind(Enum):
    """
    The facility kind, (for example, wellbore, pipeline, etc).

    :cvar GENERIC: The calibration affects the acquisition which runs
        neither inside a well or a pipeline.
    :cvar PIPELINE: The calibration affects the acquisition which runs
        inside a pipeline.
    :cvar WELLBORE:
    """
    GENERIC = "generic"
    PIPELINE = "pipeline"
    WELLBORE = "wellbore"
