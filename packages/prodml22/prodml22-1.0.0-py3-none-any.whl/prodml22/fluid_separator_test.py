from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_separator_test_step import FluidSeparatorTestStep
from prodml22.fluid_volume_reference import FluidVolumeReference
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.saturation_pressure import SaturationPressure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSeparatorTest:
    """
    FluidSeparator  Test.

    :ivar test_number: A number for this test for purposes of, e.g.,
        tracking lab sequence.
    :ivar reservoir_temperature: The reservoir temperature for this
        test.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar saturated_oil_formation_volume_factor: The saturated oil
        formation volume factor for this test.
    :ivar saturated_oil_density: The saturated oil density for this
        test.
    :ivar separator_test_gor: The separator test GOR for this test.
    :ivar overall_gas_gravity: The overall gas gravity for this test.
    :ivar remark: Remarks and comments about this data item.
    :ivar shrinkage_reference:
    :ivar separator_test_step:
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
    reservoir_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReservoirTemperature",
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
    saturated_oil_formation_volume_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SaturatedOilFormationVolumeFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    saturated_oil_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SaturatedOilDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    separator_test_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SeparatorTestGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    overall_gas_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "OverallGasGravity",
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
    shrinkage_reference: Optional[FluidVolumeReference] = field(
        default=None,
        metadata={
            "name": "ShrinkageReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    separator_test_step: List[FluidSeparatorTestStep] = field(
        default_factory=list,
        metadata={
            "name": "SeparatorTestStep",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
