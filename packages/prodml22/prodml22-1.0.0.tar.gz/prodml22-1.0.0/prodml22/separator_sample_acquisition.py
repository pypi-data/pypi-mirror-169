from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SeparatorSampleAcquisition(FluidSampleAcquisition):
    """
    Additonal information required from a fluid sample taken from a separator.

    :ivar separator: A reference to the separator where this sample was
        taken.
    :ivar well_completion: A reference to a well completion (WITSML data
        object) where this sample was taken.
    :ivar separator_pressure: The separator pressure when this sample
        was taken.
    :ivar separator_temperature: The separator temperature when this
        sample was taken.
    :ivar sampling_point: A reference to the flow port in the facility
        where this sample was taken.
    :ivar corrected_oil_rate: The corrected oil rate for this separator
        sample acquisition.
    :ivar corrected_gas_rate: The corrected gas rate for this separator
        sample acquisition.
    :ivar corrected_water_rate: The corrected water rate for this
        separator sample acquisition.
    :ivar measured_oil_rate: The measured oil rate for this separator
        sample acquisition.
    :ivar measured_gas_rate: The measured gas rate for this separator
        sample acquisition.
    :ivar measured_water_rate: The measured water rate for this
        separator sample acquisition.
    :ivar flow_test_activity:
    """
    separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Separator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
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
    separator_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "SeparatorPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    separator_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "SeparatorTemperature",
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
    corrected_oil_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CorrectedOilRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    corrected_gas_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CorrectedGasRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    corrected_water_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CorrectedWaterRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_oil_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MeasuredOilRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_gas_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MeasuredGasRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_water_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MeasuredWaterRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
