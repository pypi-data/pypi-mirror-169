from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.fluid_analysis_step_condition import FluidAnalysisStepCondition
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OtherMeasurementTestStep:
    """
    Other measurement test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_pressure: The pressure for this test step.
    :ivar step_temperature: The temperature for this test step.
    :ivar oil_viscosity: The viscosity of the oil phase at this test
        step.
    :ivar oil_mass_density: The oil mass density for this test step.
    :ivar gas_viscosity: The viscosity of the gas phase at this test
        step.
    :ivar gas_gravity: The gas gravity at this test step.
    :ivar gas_mass_density: The gas density at this test step.
    :ivar gas_zfactor: The gas Z factor value at this test step.
    :ivar fluid_condition: The fluid condition at this test step. Enum,
        see fluid analysis step condition.
    :ivar water_content: The water content for this test step.
    :ivar water_viscosity: The water viscosity for this test step.
    :ivar salinity: The salinity for this test step.
    :ivar rsw: The rsw for this test step.
    :ivar shear: The shear for this test step.
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
        }
    )
    step_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "StepTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "OilViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_mass_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilMassDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "GasViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "GasGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_mass_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasMassDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_zfactor: Optional[float] = field(
        default=None,
        metadata={
            "name": "GasZFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_condition: Optional[FluidAnalysisStepCondition] = field(
        default=None,
        metadata={
            "name": "FluidCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaterContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    salinity: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    rsw: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rsw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    shear: Optional[float] = field(
        default=None,
        metadata={
            "name": "Shear",
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
