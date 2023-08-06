from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_differential_liberation_test_step import FluidDifferentialLiberationTestStep
from prodml22.fluid_volume_reference import FluidVolumeReference
from prodml22.saturation_pressure import SaturationPressure
from prodml22.separator_conditions import SeparatorConditions
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DifferentialLiberationTest:
    """
    The differential liberation test.

    :ivar test_number: A number for this test for purposes of, e.g.,
        tracking lab sequence.
    :ivar test_temperature: The temperature of this test.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar separator_conditions: Reference to a separator test element
        that contains the separator conditions (stages) that apply to
        this test.
    :ivar correction_method: A flag to indicate if differential
        liberation/vaporization data are corrected to separator
        conditions/flash data or not.
    :ivar remark: Remarks and comments about this data item.
    :ivar shrinkage_reference:
    :ivar dl_test_step:
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
            "required": True,
        }
    )
    separator_conditions: Optional[SeparatorConditions] = field(
        default=None,
        metadata={
            "name": "SeparatorConditions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    correction_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrectionMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    dl_test_step: List[FluidDifferentialLiberationTestStep] = field(
        default_factory=list,
        metadata={
            "name": "DlTestStep",
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
