from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CustomPvtModelParameter:
    """
    Custom PVT model parameter.

    :ivar custom_parameter_value:
    :ivar fluid_component_reference: Reference to a fluid component to
        which this custom model parameter applies.
    """
    custom_parameter_value: Optional[ExtensionNameValue] = field(
        default=None,
        metadata={
            "name": "CustomParameterValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fluid_component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponentReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
