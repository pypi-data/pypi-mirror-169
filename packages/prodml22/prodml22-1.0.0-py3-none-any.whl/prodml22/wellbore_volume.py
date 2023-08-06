from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellboreVolume(AbstractParameter):
    """The volume of the wellbore equipment which influences the wellbore
    storage.

    It will be sum of volumes of all components open to the reservoir up
    to the shut off valve.
    """
    abbreviation: str = field(
        init=False,
        default="Vw",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
