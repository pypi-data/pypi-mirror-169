from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Aggregate(AbstractObject):
    """An Energistics data object that is an aggregate of other data objects.

    Use Case: You want to email someone several different Energistics
    data objects (which are each separate XML files) from one or more of
    the Energistics domain standards. You can group those data objects
    together using Aggregate. This object is NOT INTENDED for use within
    an ML (e.g. a WITSML) data store, even though it is  constructed
    similarly to the standard data object pattern. The anticipated
    normal usage is for collecting an aggregate of object messages for
    transport outside the context of an ML store. This data object was
    first developed by WITSML but has been "promoted" to Energistics
    common for use by any of the Energistics domain standards.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    aggregate_member: List[AbstractObject] = field(
        default_factory=list,
        metadata={
            "name": "AggregateMember",
            "type": "Element",
            "min_occurs": 1,
        }
    )
