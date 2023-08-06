from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.fiber_common import FiberCommon
from prodml22.fiber_splice_kind import FiberSpliceKind
from prodml22.plane_angle_uom import PlaneAngleUom
from prodml22.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberSplice(FiberCommon):
    """
    A splice component within the optical path.

    :ivar splice_equipment_used_reference: A useful description of the
        equipment used to create the splice.
    :ivar stripping_type: A useful description of the stripping type
        that was conducted.
    :ivar protector_type: A useful description of the type of protector
        used in the splice.
    :ivar fiber_splice_type: Enum. The type of splice.
    :ivar pressure_rating: The pressure rating for which the splice is
        expected to withstand.
    :ivar bend_angle: The measurement of the bend on the splice.
    """
    splice_equipment_used_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpliceEquipmentUsedReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    stripping_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrippingType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    protector_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProtectorType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    fiber_splice_type: Optional[FiberSpliceKind] = field(
        default=None,
        metadata={
            "name": "FiberSpliceType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    pressure_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PressureRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bend_angle: Optional[PlaneAngleUom] = field(
        default=None,
        metadata={
            "name": "BendAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
