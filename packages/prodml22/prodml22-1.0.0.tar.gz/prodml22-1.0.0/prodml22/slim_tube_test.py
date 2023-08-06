from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.slim_tube_specification import SlimTubeSpecification
from prodml22.slim_tube_test_step import SlimTubeTestStep
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SlimTubeTest:
    """Attributes of a slim-tube test.

    For definition of a slim-tube test, see http://www.glossary.oilfield.slb.com/Terms/s/slim-tube_test.aspx

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar test_temperature: The temperature of this test.
    :ivar pump_temperature: The pump temperature during the slim-tube
        test.
    :ivar remark: Remarks and comments about this data item.
    :ivar slim_tube_test_pressure_step:
    :ivar slim_tube_specification:
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
    pump_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "PumpTemperature",
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
    slim_tube_test_pressure_step: List[SlimTubeTestStep] = field(
        default_factory=list,
        metadata={
            "name": "SlimTubeTestPressureStep",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    slim_tube_specification: List[SlimTubeSpecification] = field(
        default_factory=list,
        metadata={
            "name": "SlimTubeSpecification",
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
