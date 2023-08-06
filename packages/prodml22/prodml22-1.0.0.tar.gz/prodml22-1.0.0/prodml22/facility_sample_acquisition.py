from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FacilitySampleAcquisition(FluidSampleAcquisition):
    """
    Additional information required for a sample taken from a facility.

    :ivar sampling_point: A reference to the flow port in the facility
        where this sample was taken.
    :ivar facility_pressure: The facility pressure for this facility
        sample acquisition.
    :ivar facility_temperature: The facility temperature when this
        sample was taken.
    :ivar facility:
    """
    sampling_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "SamplingPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    facility_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "FacilityPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FacilityTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
