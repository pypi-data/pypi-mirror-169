from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.axis_order2d import AxisOrder2D
from prodml22.east_or_west import EastOrWest
from prodml22.north_or_south import NorthOrSouth
from prodml22.principal_meridian import PrincipalMeridian

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PublicLandSurveySystemLocation:
    """
    Land survey system that describes the well by range, township, section,
    etc.

    :ivar principal_meridian: Principal meridian for this location.
    :ivar range: Range number.
    :ivar range_dir: Range direction.
    :ivar township: Township number.
    :ivar township_dir: Township direction.
    :ivar section: Section number.
    :ivar quarter_section: The location of the well within the section,
        with the primary component listed first. Spot location will be
        made from a combinationof the following codes: NE, NW, SW, SE,
        N2, S2, E2, W2, C (center quarter), LTxx (where xx represents a
        two digit lot designation), TRzz (where zz represents a one or
        two character trac designation). Free format allows for entries
        such as NESW (southwest quarter of northeast quarter), E2NESE
        (southeast quarter of northeast quarter of east half), CNE
        (northeast quarter of center quarter), etc.
    :ivar quarter_township: Quarter township.
    :ivar axis_order:
    """
    principal_meridian: Optional[PrincipalMeridian] = field(
        default=None,
        metadata={
            "name": "PrincipalMeridian",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    range: Optional[int] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    range_dir: Optional[EastOrWest] = field(
        default=None,
        metadata={
            "name": "RangeDir",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    township: Optional[int] = field(
        default=None,
        metadata={
            "name": "Township",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    township_dir: Optional[NorthOrSouth] = field(
        default=None,
        metadata={
            "name": "TownshipDir",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "name": "Section",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
            "pattern": r"[+]?([1-9]|[1-2][0-9]|3[0-6])\.?[0-9]?",
        }
    )
    quarter_section: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuarterSection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
            "pattern": r"(NE|NW|SW|SE|N2|S2|E2|W2|C|LT[0-9]{2,2}|TR[a-zA-Z0-9]{1,2}){1,3}",
        }
    )
    quarter_township: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuarterTownship",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
            "pattern": r"NE|NW|SW|SE",
        }
    )
    axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "AxisOrder",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
