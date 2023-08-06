from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.thermodynamic_temperature_measure_ext import ThermodynamicTemperatureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReferenceSeparatorStage:
    """
    Reference to the separator stage.

    :ivar separator_pressure: The separator pressure for a separator
        stage used to define the separation train, which is used as the
        basis of this fluid characterization.
    :ivar separator_temperature: The separator temperature for a
        separator stage used to define the separation train, which is
        used as the basis of this fluid characterization.
    :ivar separator_number: The separator number for a separator stage
        used to define the separation train, which is used as the basis
        of this fluid characterization.
    """
    separator_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "SeparatorPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    separator_temperature: Optional[ThermodynamicTemperatureMeasureExt] = field(
        default=None,
        metadata={
            "name": "SeparatorTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    separator_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeparatorNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
