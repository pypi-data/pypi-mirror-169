from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.fluid_analysis_step_condition import FluidAnalysisStepCondition
from prodml22.liquid_composition import LiquidComposition
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.oil_compressibility import OilCompressibility
from prodml22.overall_composition import OverallComposition
from prodml22.phase_present import PhasePresent
from prodml22.pressure_measure import PressureMeasure
from prodml22.reciprocal_pressure_measure import ReciprocalPressureMeasure
from prodml22.relative_volume_ratio import RelativeVolumeRatio
from prodml22.vapor_composition import VaporComposition
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConstantCompositionExpansionTestStep:
    """
    The CCE test steps.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_pressure: The pressure for this test step.
    :ivar liquid_fraction: The fraction of liquid by volume for this
        test step. This is the volume of liquid divided by a reference
        volume. Refer to the documentation for the Relative Volume Ratio
        and Fluid Volume Reference classes.
    :ivar oil_density: The density of the oil phase at this test step.
    :ivar oil_compressibility: The oil compressibility at this test
        step.
    :ivar oil_viscosity: The viscosity of the oil phase at this test
        step.
    :ivar total_volume: The total volume of the expanded mixture at this
        test step.
    :ivar relative_volume_ratio: Measured relative volume ratio =
        measured volume/volume at Psat.
    :ivar gas_density: The gas density at the conditions for this
        viscosity correlation to be used.
    :ivar gas_zfactor: The gas Z factor value at this test step.
    :ivar gas_compressibility: The gas compressibility at this test
        step.
    :ivar gas_viscosity: The viscosity of the gas phase at this test
        step.
    :ivar yfunction: The Y function at this test step. See  Standing,
        M.B.: Volumetric And Phase Behavior Of Oil Field Hydrocarbon
        Systems, Eighth Edition, SPE Richardson, Texas (1977).
    :ivar fluid_condition: The fluid condition at this test step. Enum,
        see fluid analysis step condition.
    :ivar phases_present: The phases present at this test step (oil,
        water, gas etc.). Enum, see phases present.
    :ivar vapor_composition: The vapor composition at this test step.
    :ivar liquid_composition: The liquid composition at this test step.
    :ivar overall_composition: The overall composition at this test
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
    step_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StepPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    liquid_fraction: Optional[RelativeVolumeRatio] = field(
        default=None,
        metadata={
            "name": "LiquidFraction",
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
    oil_compressibility: Optional[OilCompressibility] = field(
        default=None,
        metadata={
            "name": "OilCompressibility",
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
    total_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    relative_volume_ratio: Optional[RelativeVolumeRatio] = field(
        default=None,
        metadata={
            "name": "RelativeVolumeRatio",
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
    gas_compressibility: Optional[ReciprocalPressureMeasure] = field(
        default=None,
        metadata={
            "name": "GasCompressibility",
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
    yfunction: Optional[float] = field(
        default=None,
        metadata={
            "name": "YFunction",
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
    vapor_composition: Optional[VaporComposition] = field(
        default=None,
        metadata={
            "name": "VaporComposition",
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
