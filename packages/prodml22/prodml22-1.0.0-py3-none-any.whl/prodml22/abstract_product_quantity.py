from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_measure import AmountOfSubstanceMeasure
from prodml22.mass_measure import MassMeasure
from prodml22.volume_value import VolumeValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractProductQuantity:
    """
    The Abstract base type of product quantity.

    :ivar volume: The amount of product as a volume measure.
    :ivar mass: The amount of product as a mass measure.
    :ivar moles: Moles.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    volume: Optional[VolumeValue] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    moles: Optional[AmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "Moles",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
