from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.endpoint_qualifier import EndpointQualifier

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class EndpointQualifiedDateTime:
    """A timestamp value used for min/max query parameters related to "growing
    objects".

    The meaning of the endpoint of an interval can be modified by the
    endpoint attribute.

    :ivar endpoint: The default is "inclusive".
    """
    endpoint: Optional[EndpointQualifier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
