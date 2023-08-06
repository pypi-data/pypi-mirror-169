from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.fluid_component_property import FluidComponentProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ComponentPropertySet:
    """
    Component property set.

    :ivar fluid_component_property: The properties of a fluid component.
    """
    fluid_component_property: List[FluidComponentProperty] = field(
        default_factory=list,
        metadata={
            "name": "FluidComponentProperty",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
