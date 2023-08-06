from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractRefProductFlow:
    """A reference to a flow within the current product volume report.

    This represents a foreign key from one element to another.
    """
