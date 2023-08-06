from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fiber_facility import AbstractFiberFacility

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberFacilityGeneric(AbstractFiberFacility):
    """
    If a facility mapping is not explicitly to a well or pipeline, use this
    element to show what optical path distances map to lengths in a generic
    facility.

    :ivar facility_name: The name or description of the facility.
    :ivar facility_kind: A comment to describe this facility.
    """
    facility_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    facility_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
