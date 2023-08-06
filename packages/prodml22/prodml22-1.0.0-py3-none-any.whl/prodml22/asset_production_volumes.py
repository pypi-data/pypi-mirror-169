from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_simple_product_volume import AbstractSimpleProductVolume
from prodml22.reporting_duration_kind import ReportingDurationKind
from prodml22.reporting_entity_volumes import ReportingEntityVolumes

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AssetProductionVolumes(AbstractSimpleProductVolume):
    """Contains all volume data for all reporting entities (e.g., area, field,
    wells, etc.).

    Although named "volumes" in line with industry usage, different
    quantities may be reported, such as volume, mass, and energy
    content.

    :ivar start_date: The start date of the reporting period.
    :ivar end_date: The end date of report period.
    :ivar nominal_period: Nominal period.
    :ivar reporting_entity_volumes: Contains all the volumes for a
        single reporting entity. It contains a reference back to the
        reporting entity using its UUID for reference.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    nominal_period: Optional[Union[ReportingDurationKind, str]] = field(
        default=None,
        metadata={
            "name": "NominalPeriod",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    reporting_entity_volumes: List[ReportingEntityVolumes] = field(
        default_factory=list,
        metadata={
            "name": "ReportingEntityVolumes",
            "type": "Element",
        }
    )
