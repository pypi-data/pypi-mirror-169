from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_measure_ext import LengthMeasureExt
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSampleAcquisition:
    """Information common to any fluid sample taken.

    Additional details can be captured in related data object depending
    on the where the sample was taken, for example: downhole, separator,
    wellhead, of the formation using a wireline formation tester (WFT).
    If the tool used to capture samples has multiple containers, each
    container has a separate instance of fluid sample acquisition.

    :ivar start_time: The date when the sample was taken.
    :ivar end_time:
    :ivar acquisition_pressure: The acquisition pressure when this
        sample was taken.
    :ivar acquisition_temperature: The acquisition temperature when this
        sample was taken. .
    :ivar acquisition_volume: The acquisition volume when this sample
        was taken.
    :ivar acquisition_gor: The acquisition gas-oil ratio for this fluid
        sample acquisition.
    :ivar formation_pressure_temperature_datum: The datum depth for
        which the Formation Pressure and Formation Temperature data
        applies.
    :ivar formation_pressure: The formation pressure when this sample
        was taken.
    :ivar formation_temperature: The formation temperature when this
        sample was taken.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_sample_container:
    :ivar fluid_sample:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    acquisition_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "AcquisitionPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    acquisition_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "AcquisitionTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    acquisition_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AcquisitionVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    acquisition_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AcquisitionGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    formation_pressure_temperature_datum: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "FormationPressureTemperatureDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    formation_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FormationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    formation_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FormationTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    fluid_sample_container: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSampleContainer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fluid_sample: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSample",
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
            "max_length": 64,
        }
    )
