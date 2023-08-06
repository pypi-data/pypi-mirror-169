from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReportingHierarchyNode:
    """
    Association that contains the parent and child of this node.

    :ivar child_node:
    :ivar reporting_entity:
    :ivar id: The identification of node.
    :ivar name: The entity name.
    """
    child_node: List["ReportingHierarchyNode"] = field(
        default_factory=list,
        metadata={
            "name": "ChildNode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reporting_entity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReportingEntity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
