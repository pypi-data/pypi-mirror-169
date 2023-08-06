from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.reciprocal_pressure_measure_ext import ReciprocalPressureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellboreFluidCompressibility(AbstractParameter):
    """The compressibility of the fluid in the wellbore, such that this value * wellbore volume = wellbore storage coefficient."""
    abbreviation: str = field(
        init=False,
        default="Cw",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    compressibility: Optional[ReciprocalPressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "Compressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
