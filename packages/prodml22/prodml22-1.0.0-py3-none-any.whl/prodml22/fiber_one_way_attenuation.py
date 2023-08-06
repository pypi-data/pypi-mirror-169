from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_attenuation_measure import AbstractAttenuationMeasure
from prodml22.logarithmic_power_ratio_per_length_measure import LogarithmicPowerRatioPerLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOneWayAttenuation:
    """The power loss for one-way travel of a beam of light, usually measured
    in decibels per unit length.

    It is necessary to include both the value (and its unit) and the
    wavelength at which this attenuation was measured.

    :ivar value: The value of the one-way loss per unit of length. The
        usual UOM is decibels per kilometer (dB/km) although this might
        vary depending on the calibration method used.
    :ivar attenuation_measure:
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
    attenuation_measure: Optional[AbstractAttenuationMeasure] = field(
        default=None,
        metadata={
            "name": "AttenuationMeasure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
