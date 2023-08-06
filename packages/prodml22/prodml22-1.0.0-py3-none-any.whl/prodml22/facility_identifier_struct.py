from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.reporting_facility import ReportingFacility

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FacilityIdentifierStruct:
    """
    Identifies a facility.

    :ivar kind: The kind of facility.
    :ivar site_kind: A custom sub-categorization of facility kind. This
        attribute is free-form text and allows implementers to provide a
        more specific or specialized description of the facility kind.
    :ivar naming_system: The naming system within which the name is
        unique. For example, API or NPD.
    :ivar uid_ref: The referencing uid.
    :ivar content:
    """
    kind: Optional[ReportingFacility] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    site_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "siteKind",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    naming_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "namingSystem",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    uid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uidRef",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
