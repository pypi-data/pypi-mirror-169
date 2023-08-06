from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.boundary1_type import Boundary1Type
from prodml22.boundary_base_model import BoundaryBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ClosedCircleModel(BoundaryBaseModel):
    """
    Closed circle boundary model.
    """
    boundary1_type: Optional[Boundary1Type] = field(
        default=None,
        metadata={
            "name": "Boundary1Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
