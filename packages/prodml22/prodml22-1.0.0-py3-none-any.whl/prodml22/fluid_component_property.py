from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molar_volume_measure import MolarVolumeMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.reciprocal_pressure_measure import ReciprocalPressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidComponentProperty:
    """
    The properties of a fluid component.

    :ivar critical_pressure: The critical pressure for this fluid
        component.
    :ivar critical_temperature: The critical temperature for this fluid
        component.
    :ivar critical_viscosity: The critical viscosity for this fluid
        component.
    :ivar compact_volume: The compact volume for this fluid component.
    :ivar critical_volume: The critical volume for this fluid component.
    :ivar acentric_factor: The acentric factor for this fluid component.
    :ivar mass_density: The mass density for this fluid component.
    :ivar omega_a: The omega A for this fluid component.
    :ivar omega_b: The omega B for this fluid component.
    :ivar volume_shift_parameter: The volume shift parameter for this
        fluid component.
    :ivar partial_molar_density: The partial molar density for this
        fluid component.
    :ivar parachor: The parachor for this fluid component.
    :ivar partial_molar_volume: The partial molar volume for this fluid
        component.
    :ivar reference_density_zj: The reference density for this fluid
        component.
    :ivar reference_gravity_zj: The reference gravity for this fluid
        component.
    :ivar reference_temperature_zj: The reference temperature for this
        fluid component.
    :ivar viscous_compressibility: The viscous compressibility for this
        fluid component.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_component_reference: The reference to the fluid
        component to which these properties apply.
    """
    critical_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "CriticalPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    critical_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "CriticalTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    critical_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "CriticalViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    compact_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CompactVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    critical_volume: Optional[MolarVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CriticalVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    acentric_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "AcentricFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MassDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    omega_a: Optional[float] = field(
        default=None,
        metadata={
            "name": "OmegaA",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    omega_b: Optional[float] = field(
        default=None,
        metadata={
            "name": "OmegaB",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_shift_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "VolumeShiftParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    partial_molar_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PartialMolarDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    parachor: Optional[float] = field(
        default=None,
        metadata={
            "name": "Parachor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    partial_molar_volume: Optional[MolarVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PartialMolarVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_density_zj: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceDensityZJ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_gravity_zj: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceGravityZJ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_temperature_zj: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceTemperatureZJ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    viscous_compressibility: Optional[ReciprocalPressureMeasure] = field(
        default=None,
        metadata={
            "name": "ViscousCompressibility",
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
    fluid_component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponentReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
