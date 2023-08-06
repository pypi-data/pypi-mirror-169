from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlowTestActivity(AbstractObject):
    """Describes the measurement set of  a single flow test activity.

    In most types of tests, this measurement set is obtained at one
    interval (an interval being a connection to reservoir). In
    interference tests (vertical or interwell) there will be more than 1
    interval, each with its own measurement set. This object is
    abstract; you must choose one of the available types.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"
