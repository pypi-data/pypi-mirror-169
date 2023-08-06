from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_pvt_model import AbstractPvtModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCorrelationModel(AbstractPvtModel):
    """
    Abstract class of correlation model.
    """
