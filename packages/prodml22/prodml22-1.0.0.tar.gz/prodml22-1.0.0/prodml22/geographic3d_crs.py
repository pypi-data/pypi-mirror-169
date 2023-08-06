from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geographic3DCrs(AbstractObject):
    class Meta:
        name = "Geographic3dCrs"
