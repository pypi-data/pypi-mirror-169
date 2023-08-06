from __future__ import annotations
from dataclasses import dataclass
from prodml22.wellbore_base_model import WellboreBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConstantStorageModel(WellboreBaseModel):
    """
    Constant wellbore storage model.
    """
