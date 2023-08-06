from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.volume_per_pressure_measure_ext import VolumePerPressureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellboreStorageCoefficient(AbstractParameter):
    """The wellbore storage coefficient equal to the volume which flows into
    the wellbore per unit change in pressure in the wellbore.

    NOTE that by setting this parameter to = 0, the model becomes equivalent to a "No Wellbore Storage" model.
    """
    abbreviation: str = field(
        init=False,
        default="Cs",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    volume_per_pressure: Optional[VolumePerPressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "VolumePerPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
