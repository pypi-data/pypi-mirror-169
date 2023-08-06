from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.injected_gas import InjectedGas
from prodml22.swelling_test_step import SwellingTestStep
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SwellingTest:
    """
    Swelling test.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar test_temperature: The temperature of this test.
    :ivar injected_gas: The composition of one or more injected gases
        used in the swelling test.
    :ivar remark: Remarks and comments about this data item.
    :ivar swelling_test_step:
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
    injected_gas: List[InjectedGas] = field(
        default_factory=list,
        metadata={
            "name": "InjectedGas",
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
    swelling_test_step: List[SwellingTestStep] = field(
        default_factory=list,
        metadata={
            "name": "SwellingTestStep",
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
