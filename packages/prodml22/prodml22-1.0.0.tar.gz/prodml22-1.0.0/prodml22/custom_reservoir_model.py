from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.custom_parameter import CustomParameter
from prodml22.model_name import ModelName
from prodml22.reservoir_base_model import ReservoirBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CustomReservoirModel(ReservoirBaseModel):
    """
    Reservoir Model allowing for the addition of custom parameters to support
    extension of the model library provided.
    """
    model_name: Optional[ModelName] = field(
        default=None,
        metadata={
            "name": "ModelName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    any_parameter: List[AbstractParameter] = field(
        default_factory=list,
        metadata={
            "name": "AnyParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custom_parameter: List[CustomParameter] = field(
        default_factory=list,
        metadata={
            "name": "CustomParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
