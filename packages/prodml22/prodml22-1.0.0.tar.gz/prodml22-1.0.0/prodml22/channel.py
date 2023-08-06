from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Channel(AbstractObject):
    """A channel is a series of individual data points.

    A channel is comparable to a log curve; more generally, it is
    comparable to a tag in a process historian. Channels organize their
    data points according to one or more channel indexes, like time or
    depth.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"
