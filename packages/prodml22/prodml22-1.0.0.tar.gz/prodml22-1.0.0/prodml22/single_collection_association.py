from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class SingleCollectionAssociation:
    """Indicates the data objects that are associated to a single collection.

    BUSINESS RULE: The same collection CANNOT be used in multiple SingleCollectionAssociations of the same CollectionsToDataobjectsAssociations.
    BUSINESS RULE : If two or more of the same data objects are used in one SingleCollectionAssociation, only one data object should be taken into account and the other ones must be ignored.

    :ivar homogeneous_datatype: Boolean flag. If true all data objects
        in the collection are of the same Energistics data type
        (EXAMPLE: All wellbores or all horizons).
    :ivar dataobject:
    :ivar collection:
    """
    homogeneous_datatype: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomogeneousDatatype",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    dataobject: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Dataobject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
    collection: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Collection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
