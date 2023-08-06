from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_object import AbstractObject
from prodml22.single_collection_association import SingleCollectionAssociation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class CollectionsToDataobjectsAssociationSet(AbstractObject):
    """Allows data objects to be associated in one or more collections.

    BUSINESS RULE : If two or more of the same data object collections are used in one CollectionsToDataobjectsAssociationSet, only one of those data object collections should be taken into account and the other ones must be ignored.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    single_collection_association: List[SingleCollectionAssociation] = field(
        default_factory=list,
        metadata={
            "name": "SingleCollectionAssociation",
            "type": "Element",
            "min_occurs": 1,
        }
    )
