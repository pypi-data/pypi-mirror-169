from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_fluid_component import AbstractFluidComponent
from prodml22.interfacial_tension_test_step import InterfacialTensionTestStep
from prodml22.thermodynamic_phase import ThermodynamicPhase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterfacialTensionTest:
    """
    The interfacial tension test.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar wetting_phase: The wetting phase for this interfacial tension
        test.
    :ivar non_wetting_phase: The non-wetting phase for this interfacial
        tension test.
    :ivar surfactant: The surfactant for this interfacial tension test.
    :ivar remark: Remarks and comments about this data item.
    :ivar interfacial_tension_test_step: The interfacial tension test
        step.
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
    wetting_phase: Optional[ThermodynamicPhase] = field(
        default=None,
        metadata={
            "name": "WettingPhase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    non_wetting_phase: Optional[ThermodynamicPhase] = field(
        default=None,
        metadata={
            "name": "nonWettingPhase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    surfactant: Optional[AbstractFluidComponent] = field(
        default=None,
        metadata={
            "name": "Surfactant",
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
    interfacial_tension_test_step: List[InterfacialTensionTestStep] = field(
        default_factory=list,
        metadata={
            "name": "InterfacialTensionTestStep",
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
