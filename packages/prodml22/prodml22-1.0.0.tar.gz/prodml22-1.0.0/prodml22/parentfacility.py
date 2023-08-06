from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_ref_product_flow import AbstractRefProductFlow

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Parentfacility(AbstractRefProductFlow):
    """
    Parent facility.

    :ivar parentfacility_reference: A reference to a flow within the
        current product volume report. This represents a foreign key
        from one element to another.
    """
    parentfacility_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentfacilityReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
