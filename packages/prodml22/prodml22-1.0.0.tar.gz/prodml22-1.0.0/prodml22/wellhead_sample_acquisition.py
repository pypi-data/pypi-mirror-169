from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellheadSampleAcquisition(FluidSampleAcquisition):
    """
    Additional information required for a fluid sample taken from a wellhead.

    :ivar well: A reference to the well (WITSML data object) where this
        sample was taken.
    :ivar well_completion: A reference to the well completion (WITSML
        data object) where this sample was taken.
    :ivar wellhead_pressure: The wellhead pressure when the sample was
        taken.
    :ivar wellhead_temperature: The wellhead temperature when the sample
        was taken.
    :ivar sampling_point: A reference to the flow port in the facility
        where this sample was taken.
    :ivar flow_test_activity:
    """
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_completion: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellCompletion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellhead_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "WellheadPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    wellhead_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "WellheadTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    sampling_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "SamplingPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    flow_test_activity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
