from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_cvd_test_step import FluidCvdTestStep
from prodml22.fluid_volume_reference import FluidVolumeReference
from prodml22.saturation_pressure import SaturationPressure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConstantVolumeDepletionTest:
    """
    The CVT test.

    :ivar test_number: A number for this test for purposes of, e.g.,
        tracking lab sequence.
    :ivar test_temperature: The temperature of this test.
    :ivar cumulative_gas_produced_reference_std: The volume is corrected
        to standard conditions of temperature and pressure.
    :ivar remark: Remarks and comments about this data item.
    :ivar saturation_pressure:
    :ivar liquid_fraction_reference:
    :ivar cvd_test_step:
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
    cumulative_gas_produced_reference_std: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeGasProducedReferenceStd",
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
    cvd_test_step: List[FluidCvdTestStep] = field(
        default_factory=list,
        metadata={
            "name": "CvdTestStep",
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
