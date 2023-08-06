from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.fluid_component_fraction import FluidComponentFraction
from prodml22.injected_gas import InjectedGas
from prodml22.liquid_composition import LiquidComposition
from prodml22.phase_density import PhaseDensity
from prodml22.phase_viscosity import PhaseViscosity
from prodml22.pressure_measure import PressureMeasure
from prodml22.ref_injected_gas_added import RefInjectedGasAdded
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class VaporLiquidEquilibriumTest:
    """
    Properties and results for a vapor-liquid equilibrium (VLE) test.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar test_temperature: The temperature of this test.
    :ivar test_pressure: The pressure of this test.
    :ivar gas_solvent_added: The gas solvent added for this VLE test.
    :ivar mixture_volume: The mixture volume for this VLE test.
    :ivar mixture_gas_solvent_mole_fraction: The mixture gas solvent
        mole fraction for this VLE test.
    :ivar mixture_gor: The mixture gas-oil ratio for this VLE test.
    :ivar mixture_psat_test_temperature: The mixture saturation pressure
        test temperature for this VLE test.
    :ivar mixture_relative_volume_relative_to_psat: The mixture relative
        volume relative to volume a saturation pressure for this VLE
        test.
    :ivar atmospheric_flash_test_reference: Reference to the atmospheric
        flash test for this VLE test.
    :ivar injected_gas_added: Reference to the injected gas added for
        this VLE test.
    :ivar cumulative_gas_added: Reference to the cumulative gas added
        for this VLE test.
    :ivar vapor_phase_volume: The vapor phase volume for this VLE test.
    :ivar vapor_phase_viscosity: The vapor phase viscosity for this VLE
        test.
    :ivar vapor_phase_density: The vapor phase density for this VLE
        test.
    :ivar liquid_phase_volume: The liquid phase volume for this VLE
        test.
    :ivar liquid_phase_density: The liquid phase density for this VLE
        test.
    :ivar vapor_composition: The vapor composition for this VLE test.
    :ivar vapor_transport_test_reference: A reference to a vapor
        transport property test associated with this VLE test.
    :ivar liquid_transport_test_reference: A reference to a liquid
        transport property test associated with this VLE test.
    :ivar liquid_composition: The liquid composition for this VLE test.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    test_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "TestNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    test_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    test_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "TestPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_solvent_added: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasSolventAdded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mixture_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MixtureVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mixture_gas_solvent_mole_fraction: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "MixtureGasSolventMoleFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mixture_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MixtureGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mixture_psat_test_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "MixturePsatTestTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mixture_relative_volume_relative_to_psat: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MixtureRelativeVolumeRelativeToPsat",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    atmospheric_flash_test_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "AtmosphericFlashTestReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    injected_gas_added: Optional[InjectedGas] = field(
        default=None,
        metadata={
            "name": "InjectedGasAdded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cumulative_gas_added: Optional[RefInjectedGasAdded] = field(
        default=None,
        metadata={
            "name": "CumulativeGasAdded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_phase_volume: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VaporPhaseVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_phase_viscosity: Optional[PhaseViscosity] = field(
        default=None,
        metadata={
            "name": "VaporPhaseViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    vapor_phase_density: List[PhaseDensity] = field(
        default_factory=list,
        metadata={
            "name": "VaporPhaseDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    liquid_phase_volume: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LiquidPhaseVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    liquid_phase_density: Optional[PhaseDensity] = field(
        default=None,
        metadata={
            "name": "LiquidPhaseDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    vapor_composition: List[FluidComponentFraction] = field(
        default_factory=list,
        metadata={
            "name": "VaporComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_transport_test_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "VaporTransportTestReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    liquid_transport_test_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "LiquidTransportTestReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    liquid_composition: List[LiquidComposition] = field(
        default_factory=list,
        metadata={
            "name": "LiquidComposition",
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
