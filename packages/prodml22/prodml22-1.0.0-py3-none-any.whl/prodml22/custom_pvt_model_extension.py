from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.custom_pvt_model_parameter import CustomPvtModelParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CustomPvtModelExtension:
    """
    Custom PVT model extension.

    :ivar description: A description of the custom model.
    :ivar custom_pvt_model_parameter: Custom PVT model parameter.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    custom_pvt_model_parameter: List[CustomPvtModelParameter] = field(
        default_factory=list,
        metadata={
            "name": "CustomPvtModelParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
