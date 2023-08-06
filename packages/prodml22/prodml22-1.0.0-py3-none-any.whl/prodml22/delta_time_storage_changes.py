from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeltaTimeStorageChanges(AbstractParameter):
    """
    In models in which the wellbore storage coefficient changes, the time at
    which the intial wellbore storage coefficient changes to the final
    coefficient.
    """
    abbreviation: str = field(
        init=False,
        default="dT",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
