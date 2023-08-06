from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fiber_facility import AbstractFiberFacility
from prodml22.data_object_reference import DataObjectReference
from prodml22.reference_point_kind import ReferencePointKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberFacilityWell(AbstractFiberFacility):
    """
    If facility mapping is to a wellbore, this element shows what optical path
    distances map to wellbore measured depths.

    :ivar name: The name of this facilityMapping instance.
    :ivar well_datum: A reference to the wellDatum from which the
        facilityLength (i.e., in this case, depth of a wellbore being
        mapped) is measured from.
    :ivar wellbore:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    well_datum: Optional[ReferencePointKind] = field(
        default=None,
        metadata={
            "name": "WellDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
