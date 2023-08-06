from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.facility_identifier_struct import FacilityIdentifierStruct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractRelatedFacilityObject:
    """
    The abstract base type of related facility.
    """
    facility_parent: Optional["FacilityParent"] = field(
        default=None,
        metadata={
            "name": "FacilityParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )


@dataclass
class FacilityParent(AbstractRelatedFacilityObject):
    """
    Facility parent.

    :ivar name: The name of the facility. The name can be qualified by a
        naming system. This can also define the kind of facility.
    :ivar facility_parent1: For facilities whose name is unique within
        the context of another facility, the name of the parent
        facility. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar facility_parent2: For facilities whose name is unique within
        the context of another facility, the name of the parent facility
        of parent1. The name can be qualified by a naming system. This
        also defines the kind of facility.
    """
    name: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_parent1: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    facility_parent2: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
