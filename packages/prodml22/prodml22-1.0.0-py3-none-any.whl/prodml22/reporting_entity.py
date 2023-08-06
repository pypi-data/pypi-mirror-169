from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.reporting_entity_kind import ReportingEntityKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReportingEntity(AbstractObject):
    """
    Reporting Entity: The top-level entity in hierarchy structure.

    :ivar kind: The type of reporting entity.
    :ivar associated_facility: If the Reporting Entity is a facility,
        then this element can be used to include that Facility object.
        In later versions of PRODML, this may be extended to a full
        description.  Currently it is restricted to having a type.
    :ivar associated_object: If the Reporting Entity is a subsurface
        entity such as well, wellbore, well completion, wellbore
        completion, contact interval or rock-fluid unit feature which
        can be described with a specific Energistics object, then this
        element can be used to reference that object.  This uses a Data
        Object reference.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    kind: Optional[ReportingEntityKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
        }
    )
    associated_facility: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "AssociatedFacility",
            "type": "Element",
        }
    )
    associated_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "AssociatedObject",
            "type": "Element",
        }
    )
