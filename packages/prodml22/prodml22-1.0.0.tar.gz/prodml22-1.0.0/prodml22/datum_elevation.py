from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_elevation import AbstractElevation
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DatumElevation(AbstractElevation):
    """
    :ivar datum: The datum the elevation is referenced to.
    """
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
