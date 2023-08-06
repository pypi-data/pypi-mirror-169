from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_related_facility_object import AbstractRelatedFacilityObject
from prodml22.reporting_facility import ReportingFacility

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeRelatedFacility:
    """A second facility related to this flow.

    For a production flow, this would represent a role of 'produced
    for'. For an import flow, this would represent a role of 'import
    from'. For an export flow, this would represent a role of 'export
    to'.

    :ivar kind: A kind of facility where the specific name is not
        relevant.
    :ivar related_facility_object:
    """
    kind: Optional[ReportingFacility] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    related_facility_object: Optional[AbstractRelatedFacilityObject] = field(
        default=None,
        metadata={
            "name": "RelatedFacilityObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
