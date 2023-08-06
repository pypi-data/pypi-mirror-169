from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_object import AbstractObject
from prodml22.reporting_facility import ReportingFacility

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Facility(AbstractObject):
    """
    Reporting Entity: The top-level entity in hierarchy structure.

    :ivar kind: Enum for the kind of facility represented by this
        Facility.  Extensible for additional kinds.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    kind: Optional[Union[ReportingFacility, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
