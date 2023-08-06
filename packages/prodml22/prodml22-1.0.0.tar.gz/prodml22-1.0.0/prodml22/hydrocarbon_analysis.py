from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.atmospheric_flash_test_and_compositional_analysis import AtmosphericFlashTestAndCompositionalAnalysis
from prodml22.constant_composition_expansion_test import ConstantCompositionExpansionTest
from prodml22.constant_volume_depletion_test import ConstantVolumeDepletionTest
from prodml22.data_object_reference import DataObjectReference
from prodml22.differential_liberation_test import DifferentialLiberationTest
from prodml22.fluid_analysis import FluidAnalysis
from prodml22.fluid_separator_test import FluidSeparatorTest
from prodml22.interfacial_tension_test import InterfacialTensionTest
from prodml22.multiple_contact_miscibility_test import MultipleContactMiscibilityTest
from prodml22.other_measurement_test import OtherMeasurementTest
from prodml22.sample_integrity_and_preparation import SampleIntegrityAndPreparation
from prodml22.saturation_test import SaturationTest
from prodml22.slim_tube_test import SlimTubeTest
from prodml22.stoanalysis import Stoanalysis
from prodml22.swelling_test import SwellingTest
from prodml22.vapor_liquid_equilibrium_test import VaporLiquidEquilibriumTest

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class HydrocarbonAnalysis(FluidAnalysis):
    """
    A collection of any one or more fluid analyses on hydrocarbons.

    :ivar sample_integrity_and_preparation: The sample integrity and
        preparation procedure for this fluid analysis.
    :ivar atmospheric_flash_test_and_compositional_analysis: An
        atmospheric flash test and compositional analysis test within
        this fluid analysis.
    :ivar constant_composition_expansion_test: A constant composition
        expansion test within this fluid analysis.
    :ivar saturation_test: A saturation test within this fluid analysis.
    :ivar differential_liberation_test: A differential liberation test
        within this fluid analysis.
    :ivar constant_volume_depletion_test: A constant volume depletion
        test within this fluid analysis.
    :ivar separator_test: A separator test within this fluid analysis.
    :ivar transport_test: A transport test within this fluid analysis.
    :ivar vapor_liquid_equilibrium_test: A vapor liquid equilibrium test
        within this fluid analysis.
    :ivar swelling_test: A swelling test within this fluid analysis.
    :ivar slim_tube_test: A slim tube test within this fluid analysis.
    :ivar multiple_contact_miscibility_test: A multiple contact
        miscibility test within this fluid analysis.
    :ivar stoanalysis: An stock tank oil analysis within this fluid
        analysis.
    :ivar interfacial_tension_test: An interfacial tension test within
        this fluid analysis.
    :ivar fluid_sample:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    sample_integrity_and_preparation: Optional[SampleIntegrityAndPreparation] = field(
        default=None,
        metadata={
            "name": "SampleIntegrityAndPreparation",
            "type": "Element",
        }
    )
    atmospheric_flash_test_and_compositional_analysis: List[AtmosphericFlashTestAndCompositionalAnalysis] = field(
        default_factory=list,
        metadata={
            "name": "AtmosphericFlashTestAndCompositionalAnalysis",
            "type": "Element",
        }
    )
    constant_composition_expansion_test: List[ConstantCompositionExpansionTest] = field(
        default_factory=list,
        metadata={
            "name": "ConstantCompositionExpansionTest",
            "type": "Element",
        }
    )
    saturation_test: List[SaturationTest] = field(
        default_factory=list,
        metadata={
            "name": "SaturationTest",
            "type": "Element",
        }
    )
    differential_liberation_test: List[DifferentialLiberationTest] = field(
        default_factory=list,
        metadata={
            "name": "DifferentialLiberationTest",
            "type": "Element",
        }
    )
    constant_volume_depletion_test: List[ConstantVolumeDepletionTest] = field(
        default_factory=list,
        metadata={
            "name": "ConstantVolumeDepletionTest",
            "type": "Element",
        }
    )
    separator_test: List[FluidSeparatorTest] = field(
        default_factory=list,
        metadata={
            "name": "SeparatorTest",
            "type": "Element",
        }
    )
    transport_test: List[OtherMeasurementTest] = field(
        default_factory=list,
        metadata={
            "name": "TransportTest",
            "type": "Element",
        }
    )
    vapor_liquid_equilibrium_test: List[VaporLiquidEquilibriumTest] = field(
        default_factory=list,
        metadata={
            "name": "VaporLiquidEquilibriumTest",
            "type": "Element",
        }
    )
    swelling_test: List[SwellingTest] = field(
        default_factory=list,
        metadata={
            "name": "SwellingTest",
            "type": "Element",
        }
    )
    slim_tube_test: List[SlimTubeTest] = field(
        default_factory=list,
        metadata={
            "name": "SlimTubeTest",
            "type": "Element",
        }
    )
    multiple_contact_miscibility_test: List[MultipleContactMiscibilityTest] = field(
        default_factory=list,
        metadata={
            "name": "MultipleContactMiscibilityTest",
            "type": "Element",
        }
    )
    stoanalysis: List[Stoanalysis] = field(
        default_factory=list,
        metadata={
            "name": "STOAnalysis",
            "type": "Element",
        }
    )
    interfacial_tension_test: List[InterfacialTensionTest] = field(
        default_factory=list,
        metadata={
            "name": "InterfacialTensionTest",
            "type": "Element",
        }
    )
    fluid_sample: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSample",
            "type": "Element",
            "required": True,
        }
    )
