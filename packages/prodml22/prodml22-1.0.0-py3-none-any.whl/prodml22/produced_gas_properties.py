from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.vapor_composition import VaporComposition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProducedGasProperties:
    """
    The properties of produced gas.

    :ivar produced_gas_gravity: The produced gas gravity of this
        produced gas.
    :ivar vapor_composition: The vapor composition of this produced gas.
    """
    produced_gas_gravity: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "ProducedGasGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_composition: List[VaporComposition] = field(
        default_factory=list,
        metadata={
            "name": "VaporComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
