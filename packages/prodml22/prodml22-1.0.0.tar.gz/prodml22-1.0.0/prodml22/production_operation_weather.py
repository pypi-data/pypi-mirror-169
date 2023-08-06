from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.angular_velocity_measure import AngularVelocityMeasure
from prodml22.length_measure import LengthMeasure
from prodml22.plane_angle_measure import PlaneAngleMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationWeather:
    """
    Operations Weather Schema.

    :ivar dtim: Date and time the information is related to.
    :ivar agency: Name of company that supplied the data.
    :ivar barometric_pressure: Atmospheric pressure.
    :ivar beaufort_scale_number: The Beaufort wind scale is a system
        used to estimate and report wind speeds when no measuring
        apparatus is available. It was invented in the early 19th
        Century by Admiral Sir Francis Beaufort of the British Navy as a
        way to interpret winds from conditions.
    :ivar temp_surface: Average temperature above ground for the period.
        Temperature of the atmosphere.
    :ivar temp_surface_mn: Minimum temperature above ground. Temperature
        of the atmosphere.
    :ivar temp_surface_mx: Maximum temperature above ground.
    :ivar temp_wind_chill: A measure of the combined chilling effect of
        wind and low temperature on living things, also named chill
        factor, e.g., according to US Weather Service table, an air
        temperature of 30 degF with a 10 mph wind corresponds to a wind
        chill of 22 degF.
    :ivar tempsea: Sea temperature.
    :ivar visibility: Horizontal visibility.
    :ivar azi_wave: The direction from which the waves are coming,
        measured from true north.
    :ivar ht_wave: Average height of the waves.
    :ivar significant_wave: An average of the higher 1/3 of the wave
        heights passing during a sample period (typically 20 to 30
        minutes).
    :ivar max_wave: The maximum wave height.
    :ivar period_wave: The elapsed time between the passing of two wave
        tops.
    :ivar azi_wind: The direction from which the wind is blowing,
        measured from true north.
    :ivar vel_wind: Wind speed.
    :ivar type_precip: Type of precipitation.
    :ivar amt_precip: Amount of precipitation.
    :ivar cover_cloud: Description of cloud cover.
    :ivar ceiling_cloud: Height of cloud cover.
    :ivar current_sea: Current speed.
    :ivar azi_current_sea: Azimuth of current.
    :ivar comments: Comments and remarks.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    agency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    barometric_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BarometricPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    beaufort_scale_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "BeaufortScaleNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
            "max_exclusive": 12,
        }
    )
    temp_surface: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    temp_surface_mn: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempSurfaceMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    temp_surface_mx: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempSurfaceMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    temp_wind_chill: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempWindChill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tempsea: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Tempsea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    visibility: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Visibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    azi_wave: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    ht_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    significant_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SignificantWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    max_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    period_wave: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PeriodWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    azi_wind: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziWind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vel_wind: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "VelWind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    type_precip: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypePrecip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    amt_precip: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AmtPrecip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cover_cloud: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoverCloud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    ceiling_cloud: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CeilingCloud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    current_sea: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "CurrentSea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    azi_current_sea: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziCurrentSea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
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
