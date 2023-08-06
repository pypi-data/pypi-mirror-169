from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InitialPressure(AbstractParameter):
    """The initial pressure of the fluids in the reservoir layer.

    "Initial" is taken to mean "at the time at which the rate history
    used in the pressure transient analysis starts"
    """
    abbreviation: str = field(
        init=False,
        default="Pi",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
