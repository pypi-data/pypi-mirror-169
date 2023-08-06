from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MultipleContactMiscibilityTest:
    """
    Multiple contact miscibility test.

    :ivar test_number: A unique identifier for this data element. It is
        not globally unique (not a uuid) and only need be unique within
        the context of the parent top-level object.
    :ivar gas_solvent_composition_reference: The reference to the
        composition of the gas solvent that is a fluid composition.
    :ivar mix_ratio: The mix ratio for the multiple contact miscibility
        test.
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
    gas_solvent_composition_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "GasSolventCompositionReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    mix_ratio: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "MixRatio",
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
