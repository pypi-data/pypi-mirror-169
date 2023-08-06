from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationMarineOperation:
    """
    Information about a marine operation.

    :ivar dtim_start: The beginning date and time that the comment
        represents.
    :ivar dtim_end: The ending date and time that the comment
        represents.
    :ivar general_comment: A general comment on marine activity in the
        area.
    :ivar supply_ship: Name of the supply vessel for the installation.
    :ivar standby_vessel: Name of the standby vessel for the
        installation.
    :ivar supply_ship_comment: Comment regarding the supply ship.
    :ivar standby_vessel_comment: Comment regarding the standby vessel.
    :ivar activity: A comment on a special event in the marine area.
    :ivar basket_movement: Report of any basket movement to and from the
        installation.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    general_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralComment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    supply_ship: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplyShip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    standby_vessel: Optional[str] = field(
        default=None,
        metadata={
            "name": "StandbyVessel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    supply_ship_comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "SupplyShipComment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    standby_vessel_comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "StandbyVesselComment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    activity: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Activity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    basket_movement: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "BasketMovement",
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
