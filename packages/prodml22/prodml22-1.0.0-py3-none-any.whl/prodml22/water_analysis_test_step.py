from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.electric_conductivity_measure import ElectricConductivityMeasure
from prodml22.electrical_resistivity_measure_ext import ElectricalResistivityMeasureExt
from prodml22.energy_length_per_time_area_temperature_measure import EnergyLengthPerTimeAreaTemperatureMeasure
from prodml22.energy_measure import EnergyMeasure
from prodml22.energy_per_volume_measure import EnergyPerVolumeMeasure
from prodml22.flashed_gas import FlashedGas
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.mass_per_volume_per_pressure_measure_ext import MassPerVolumePerPressureMeasureExt
from prodml22.mass_per_volume_per_temperature_measure_ext import MassPerVolumePerTemperatureMeasureExt
from prodml22.molar_energy_measure import MolarEnergyMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.reciprocal_pressure_measure import ReciprocalPressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_mass_measure import VolumePerMassMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure
from prodml22.volumetric_thermal_expansion_measure import VolumetricThermalExpansionMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaterAnalysisTestStep:
    """
    Water analysis test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_pressure: The pressure for this test step.
    :ivar step_temperature: The temperature for this test step.
    :ivar dissolved_co2:
    :ivar dissolved_h2_s:
    :ivar dissolved_o2:
    :ivar flashed_gas:
    :ivar p_h:
    :ivar resistivity:
    :ivar turbidity:
    :ivar water_viscosity: The water viscosity for the water analysis
        test step.
    :ivar solution_gas_water_ratio: The solution gas-water ratio for the
        water analysis test step.
    :ivar water_viscous_compressibility: The water viscous
        compressibility for the water analysis test step.
    :ivar water_density: The water density for the water analysis test
        step.
    :ivar water_specific_heat: The water specific heat for the water
        analysis test step.
    :ivar water_formation_volume_factor: The water formation volume
        factor for the water analysis test step.
    :ivar water_heat_capacity: The water heat capacity for the water
        analysis test step.
    :ivar water_isothermal_compressibility: The water isothermal
        compressibility for the water analysis test step.
    :ivar water_thermal_conductivity: The water thermal conductivity for
        the water analysis test step.
    :ivar water_density_change_with_pressure: The water density change
        with pressure for the water analysis test step.
    :ivar water_thermal_expansion: The water thermal expansion for the
        water analysis test step.
    :ivar water_density_change_with_temperature: The water density
        change with temperature for the water analysis test step.
    :ivar water_enthalpy: The water enthalpy for the water analysis test
        step.
    :ivar water_entropy: The water entropy for the water analysis test
        step.
    :ivar water_specific_volume: The water specific volume for the water
        analysis test step.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    step_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StepNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    step_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StepPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    step_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "StepTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    dissolved_co2: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "DissolvedCO2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    dissolved_h2_s: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "DissolvedH2S",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    dissolved_o2: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "DissolvedO2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flashed_gas: Optional[FlashedGas] = field(
        default=None,
        metadata={
            "name": "FlashedGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    p_h: Optional[float] = field(
        default=None,
        metadata={
            "name": "pH",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    resistivity: Optional[ElectricalResistivityMeasureExt] = field(
        default=None,
        metadata={
            "name": "Resistivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    turbidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Turbidity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "WaterViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    solution_gas_water_ratio: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolutionGasWaterRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_viscous_compressibility: Optional[ReciprocalPressureMeasure] = field(
        default=None,
        metadata={
            "name": "WaterViscousCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_specific_heat: Optional[EnergyPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterSpecificHeat",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_formation_volume_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterFormationVolumeFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_heat_capacity: Optional[EnergyMeasure] = field(
        default=None,
        metadata={
            "name": "WaterHeatCapacity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_isothermal_compressibility: Optional[ReciprocalPressureMeasure] = field(
        default=None,
        metadata={
            "name": "WaterIsothermalCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_thermal_conductivity: Optional[ElectricConductivityMeasure] = field(
        default=None,
        metadata={
            "name": "WaterThermalConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_density_change_with_pressure: Optional[MassPerVolumePerPressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "WaterDensityChangeWithPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_thermal_expansion: Optional[VolumetricThermalExpansionMeasure] = field(
        default=None,
        metadata={
            "name": "WaterThermalExpansion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_density_change_with_temperature: Optional[MassPerVolumePerTemperatureMeasureExt] = field(
        default=None,
        metadata={
            "name": "WaterDensityChangeWithTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_enthalpy: Optional[MolarEnergyMeasure] = field(
        default=None,
        metadata={
            "name": "WaterEnthalpy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_entropy: Optional[EnergyLengthPerTimeAreaTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "WaterEntropy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_specific_volume: Optional[VolumePerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WaterSpecificVolume",
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
