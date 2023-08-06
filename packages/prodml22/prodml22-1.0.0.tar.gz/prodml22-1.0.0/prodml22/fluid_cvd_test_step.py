from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure
from prodml22.fluid_analysis_step_condition import FluidAnalysisStepCondition
from prodml22.liquid_composition import LiquidComposition
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.overall_composition import OverallComposition
from prodml22.phase_present import PhasePresent
from prodml22.pressure_measure import PressureMeasure
from prodml22.relative_volume_ratio import RelativeVolumeRatio
from prodml22.vapor_composition import VaporComposition
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure
from prodml22.volume_per_volume_measure_ext import VolumePerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCvdTestStep:
    """
    The CVD test steps.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_pressure: The pressure for this test step.
    :ivar cumulative_stock_tank_gor: The cumulative GOR at stock tank
        conditions, of all the fluid produced up and including this test
        step.
    :ivar fluid_produced_gor: The GOR of the fluid produced at this test
        step
    :ivar oil_density: The density of the oil phase at this test step.
    :ivar gas_molecular_weight: The molecular weight of the gas phase at
        this test step.
    :ivar oil_viscosity: The viscosity of the oil phase at this test
        step.
    :ivar gas_gravity: The gas gravity at this test step.
    :ivar gas_formation_volume_factor: The gas formation volume factor
        at this test step.
    :ivar gas_zfactor: The gas Z factor value at this test step.
    :ivar phase2_zfactor: The standard Z = PV/RT, but here for a two-
        phase Z-factor, use total molar volume for both phases.
    :ivar gas_viscosity: The viscosity of the gas phase at this test
        step.
    :ivar cumulative_fluid_produced_fraction: The cumulative fluid
        produced, expressed as a molar fraction of the initial quantity,
        up to and including this test step.
    :ivar liquid_fraction: The fraction of liquid by volume for this
        test step. This is the volume of liquid divided by a reference
        volume. Refer to the documentation for the Relative Volume Ratio
        and Fluid Volume Reference classes.
    :ivar fluid_condition: The fluid condition at this test step. Enum,
        see fluid analysis step condition.
    :ivar phases_present: The phases present at this test step.
    :ivar liquid_composition: The liquid composition at this test step.
    :ivar vapor_composition: The vapor composition at this test step.
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
    cumulative_stock_tank_gor: Optional[VolumePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "CumulativeStockTankGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_produced_gor: Optional[VolumePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "FluidProducedGOR ",
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
    gas_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GasMolecularWeight",
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
    gas_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "GasGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_formation_volume_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasFormationVolumeFactor",
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
    phase2_zfactor: Optional[float] = field(
        default=None,
        metadata={
            "name": "Phase2ZFactor",
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
    cumulative_fluid_produced_fraction: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeFluidProducedFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
