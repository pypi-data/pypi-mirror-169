from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_object import AbstractObject
from prodml22.reporting_hierarchy_node import ReportingHierarchyNode

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReportingHierarchy(AbstractObject):
    """
    The hierarchy structure that elements refer to in the asset registry.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    reporting_node: List[ReportingHierarchyNode] = field(
        default_factory=list,
        metadata={
            "name": "ReportingNode",
            "type": "Element",
            "min_occurs": 1,
        }
    )
