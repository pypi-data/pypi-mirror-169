from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.custom_pvt_model_extension import CustomPvtModelExtension
from prodml22.pvt_model_parameter_set import PvtModelParameterSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractPvtModel:
    """
    Abstract class of  PVT model.

    :ivar custom_pvt_model_extension: Custom PVT model extension.
    :ivar pvt_model_parameter_set: A collection of parameters.
    """
    custom_pvt_model_extension: Optional[CustomPvtModelExtension] = field(
        default=None,
        metadata={
            "name": "CustomPvtModelExtension",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pvt_model_parameter_set: Optional[PvtModelParameterSet] = field(
        default=None,
        metadata={
            "name": "PvtModelParameterSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
