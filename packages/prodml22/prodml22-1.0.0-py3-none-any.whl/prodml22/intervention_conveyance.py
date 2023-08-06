from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_cable import AbstractCable
from prodml22.intervention_conveyance_kind import InterventionConveyanceKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterventionConveyance(AbstractCable):
    """
    Information on type of intervention conveyance used by the optical path.

    :ivar intervention_conveyance_type: The type from the enumeration
        list of InterventionConveyanceType.
    :ivar comment: Comment about the intervention conveyance.
    """
    intervention_conveyance_type: Optional[InterventionConveyanceKind] = field(
        default=None,
        metadata={
            "name": "InterventionConveyanceType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
