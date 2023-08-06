from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_component_fraction import FluidComponentFraction

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LiquidComposition:
    """
    The composition of liquid.

    :ivar remark: Remarks and comments about this data item.
    :ivar liquid_component_fraction:
    """
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    liquid_component_fraction: List[FluidComponentFraction] = field(
        default_factory=list,
        metadata={
            "name": "LiquidComponentFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
