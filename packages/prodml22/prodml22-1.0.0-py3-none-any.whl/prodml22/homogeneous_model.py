from __future__ import annotations
from dataclasses import dataclass
from prodml22.reservoir_base_model import ReservoirBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class HomogeneousModel(ReservoirBaseModel):
    """
    Homogeneous reservoir model.
    """
