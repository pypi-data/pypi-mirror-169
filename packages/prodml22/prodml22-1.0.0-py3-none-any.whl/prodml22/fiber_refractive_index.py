from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.frequency_measure import FrequencyMeasure
from prodml22.length_measure import LengthMeasure
from prodml22.logarithmic_power_ratio_per_length_measure import LogarithmicPowerRatioPerLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberRefractiveIndex:
    """The refractive index of a material depends on the frequency (or
    wavelength) of the light.

    Hence, it is necessary to include both the value (a unitless number)
    and the frequency (or wavelength) it was measured at. The frequency
    will be a quantity type with a frequency unit such as Hz.

    :ivar value: The value of the refractive index.
    :ivar frequency: The frequency (and UOM) for which the refractive
        index is measured.
    :ivar wavelength: The wavelength (and UOM) for which the refractive
        index is measured. The reported wavelength should be the
        wavelength of the light in a vacuum.
    :ivar uid: Unique identifier of this object.
    """
    value: Optional[LogarithmicPowerRatioPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wavelength: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Wavelength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
