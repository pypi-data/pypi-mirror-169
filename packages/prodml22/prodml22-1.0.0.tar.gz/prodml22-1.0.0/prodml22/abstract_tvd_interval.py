from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_interval import AbstractInterval
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractTvdInterval(AbstractInterval):
    """
    :ivar tvd_min: The minimum true vertical depth value.
    :ivar tvd_max: The maximum true vertical depth value.
    :ivar uom:
    :ivar trajectory:
    """
    tvd_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "TvdMin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    tvd_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "TvdMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
