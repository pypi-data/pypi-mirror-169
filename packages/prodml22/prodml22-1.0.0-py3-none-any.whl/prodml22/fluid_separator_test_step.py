from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.fluid_analysis_step_condition import FluidAnalysisStepCondition
from prodml22.liquid_composition import LiquidComposition
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.overall_composition import OverallComposition
from prodml22.phase_present import PhasePresent
from prodml22.pressure_measure import PressureMeasure
from prodml22.saturation_pressure import SaturationPressure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.vapor_composition import VaporComposition
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSeparatorTestStep:
    """
    Fluid separator test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_temperature: The temperature for this test step.
    :ivar step_pressure: The pressure for this test step.
    :ivar bubble_point_pressure: The bubble point pressure for this test
        step.
    :ivar residual_apigravity: The residual API gravity for this test
        step.
    :ivar oil_specific_gravity: The oil specific gravity for this test
        step.
    :ivar oil_density: The density of the oil phase at this test step.
    :ivar oil_formation_volume_factor_std: The oil formation volume
        factor at standard conditions for this test step.
    :ivar oil_formation_volume_factor_corrected: The stage Oil Formation
        Volume Factor (separator corrected) for this test step.
    :ivar oil_viscosity: The viscosity of the oil phase at this test
        step.
    :ivar stage_separator_gorstd: The stage separator GOR at standard
        conditions for this test step.
    :ivar stage_separator_gorcorrected: The stage separator GOR
        (separator corrected) for this test step.
    :ivar gas_molecular_weight: The molecular weight of the gas phase at
        this test step.
    :ivar gas_gravity: The gas gravity at this test step.
    :ivar gas_density: The density of gas at this test step.
    :ivar gas_zfactor: The gas Z factor value at this test step.
    :ivar gas_viscosity: The viscosity of the gas phase at this test
        step.
    :ivar gas_volume: The gas volume for this test step.
    :ivar oil_shrinkage_factor: The oil shrinkage factor for this test
        step.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar fluid_condition: The fluid condition at this test step. Enum,
        see fluid analysis step condition.
    :ivar phases_present: The phases present for this test step. Enum,
        see phases present.
    :ivar liquid_composition: The liquid composition for this test step.
    :ivar vapor_composition: The vapor composition for this test step.
    :ivar overall_composition: The overall composition for this test
        step.
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
    step_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "StepTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
    bubble_point_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BubblePointPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    residual_apigravity: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "ResidualAPIGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_specific_gravity: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "OilSpecificGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_formation_volume_factor_std: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilFormationVolumeFactorStd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_formation_volume_factor_corrected: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilFormationVolumeFactorCorrected",
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
    stage_separator_gorstd: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StageSeparatorGORStd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    stage_separator_gorcorrected: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StageSeparatorGORCorrected",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GasMolecularWeight",
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
    gas_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasDensity",
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
    gas_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "GasViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_shrinkage_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilShrinkageFactor",
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
    fluid_condition: Optional[FluidAnalysisStepCondition] = field(
        default=None,
        metadata={
            "name": "FluidCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    phases_present: Optional[PhasePresent] = field(
        default=None,
        metadata={
            "name": "PhasesPresent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    liquid_composition: Optional[LiquidComposition] = field(
        default=None,
        metadata={
            "name": "LiquidComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_composition: Optional[VaporComposition] = field(
        default=None,
        metadata={
            "name": "VaporComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    overall_composition: Optional[OverallComposition] = field(
        default=None,
        metadata={
            "name": "OverallComposition",
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
