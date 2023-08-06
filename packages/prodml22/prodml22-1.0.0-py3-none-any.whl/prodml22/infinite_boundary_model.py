from __future__ import annotations
from dataclasses import dataclass
from prodml22.boundary_base_model import BoundaryBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InfiniteBoundaryModel(BoundaryBaseModel):
    """Infinite boundary model - there are no boundaries around the reservoir."""
