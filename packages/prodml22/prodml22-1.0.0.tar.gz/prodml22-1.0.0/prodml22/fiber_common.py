from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_dts_equipment import AbstractDtsEquipment
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberCommon(AbstractDtsEquipment):
    """
    A specialization of the equipment class containing information on
    reflectance, loss and reason for decommissioning, from which all equipment
    in the optical path inherits.

    :ivar reflectance: The fraction of incident light that is reflected
        by a fiber path component. Measured in dB.
    :ivar loss: The fraction of incident light that is lost by a fiber
        path component. Measured in dB.
    :ivar reason_for_decommissioning: Any remarks that help understand
        why the optical fiber is no longer in use.
    :ivar uid: Unique identifier of this object.
    """
    reflectance: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Reflectance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    loss: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Loss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reason_for_decommissioning: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonForDecommissioning",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
