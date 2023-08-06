from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.sample_restoration import SampleRestoration
from prodml22.saturation_pressure import SaturationPressure
from prodml22.saturation_temperature import SaturationTemperature
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SampleIntegrityAndPreparation:
    """
    Sample integrity and preparation information.

    :ivar opening_date: The date when this fluid sample was opened.
    :ivar initial_volume: The initial volume of the sample when prepared
        for analysis.
    :ivar opening_pressure: The opening pressure of the sample when
        prepared for analysis.
    :ivar opening_temperature: The opening temperature of the sample
        when prepared for analysis.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar saturation_temperature: The saturation temperature of the
        sample when prepared for analysis.
    :ivar basic_sediment_and_water: The basic sediment and water of the
        sample when prepared for analysis.
    :ivar free_water_volume: The free water volume of the sample when
        prepared for analysis.
    :ivar water_content_in_hydrocarbon: The water content in hydrocarbon
        of the sample when prepared for analysis.
    :ivar opening_remark: Remarks and comments about the opening of the
        sample.
    :ivar sample_restoration: Sample restoration.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    opening_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OpeningDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    initial_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "InitialVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    opening_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "OpeningPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    opening_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "OpeningTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    saturation_pressure: Optional[SaturationPressure] = field(
        default=None,
        metadata={
            "name": "SaturationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    saturation_temperature: Optional[SaturationTemperature] = field(
        default=None,
        metadata={
            "name": "SaturationTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    basic_sediment_and_water: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BasicSedimentAndWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    free_water_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FreeWaterVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_content_in_hydrocarbon: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WaterContentInHydrocarbon",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    opening_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "OpeningRemark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    sample_restoration: List[SampleRestoration] = field(
        default_factory=list,
        metadata={
            "name": "SampleRestoration",
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
