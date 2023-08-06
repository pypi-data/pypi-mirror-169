from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.constant_composition_expansion_test_step import ConstantCompositionExpansionTestStep
from prodml22.fluid_volume_reference import FluidVolumeReference
from prodml22.saturation_pressure import SaturationPressure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConstantCompositionExpansionTest:
    """
    The CCE test.

    :ivar test_number: A number for this test for purposes of e.g.,
        tracking lab sequence.
    :ivar test_temperature: The temperature of this test.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar liquid_fraction_reference: Volume reference for the measured
        liquid fraction in a constant composition expansion
        test. Referenced to liquid volume at saturation pressure
        (generally). At each Test Step, Liquid Fraction is the liquid
        volume at this step divided by the reference volume at the
        conditions stated in this element. An actual volume at the
        reference conditions is optional. If the reference volume is the
        total volume at that test step (i.e., it varies per test step),
        then the value "test step" would be used.
    :ivar relative_volume_reference: Volume reference for the relative
        volume ratio in a constant composition expansion
        test. Referenced to liquid volume at saturation pressure
        (generally). At each Test Step, Relative Volume Ratio is the
        total volume at this step divided by the reference volume at the
        conditions stated in this element. An actual volume at the
        reference conditions is optional.
    :ivar constant_composition_expansion_test_step: Measured relative
        volume ratio = measured volume/volume at Psat.
    :ivar remark: Expected to be a yes or no value to indicate if
        differential liberation/vaporization data are corrected to
        separator conditions/flash data or not.
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
    saturation_pressure: Optional[SaturationPressure] = field(
        default=None,
        metadata={
            "name": "SaturationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    liquid_fraction_reference: List[FluidVolumeReference] = field(
        default_factory=list,
        metadata={
            "name": "LiquidFractionReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    relative_volume_reference: List[FluidVolumeReference] = field(
        default_factory=list,
        metadata={
            "name": "RelativeVolumeReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    constant_composition_expansion_test_step: List[ConstantCompositionExpansionTestStep] = field(
        default_factory=list,
        metadata={
            "name": "ConstantCompositionExpansionTestStep",
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
