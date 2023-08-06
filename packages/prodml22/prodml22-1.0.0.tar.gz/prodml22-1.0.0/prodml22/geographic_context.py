from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.name_struct import NameStruct
from prodml22.offshore_location import OffshoreLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class GeographicContext:
    """
    A geographic context of a report.

    :ivar country: The name of the country.
    :ivar state: The state or province within the country.
    :ivar county: The name of county.
    :ivar field_value: The name of the field within whose context the
        report exists.
    :ivar comment: A general comment that further explains the offshore
        location.
    :ivar offshore_location: A generic type of offshore location. This
        allows an offshore location to be given by an area name, and up
        to four block names. A comment is also allowed.
    """
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    field_value: Optional[NameStruct] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    offshore_location: Optional[OffshoreLocation] = field(
        default=None,
        metadata={
            "name": "OffshoreLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
