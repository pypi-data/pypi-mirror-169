from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ComponentReference:
    """
    A pointer to a component within the same Energistics data object or within
    a data object pointed to by a separate data object reference.

    :ivar qualified_type: The qualified type of the referenced
        component.
    :ivar uid: The UID of the referenced component.
    :ivar name: The optional name of the referenced component.
    :ivar index: The optional numerical (i.e., NOT time or depth) index
        of the referenced component.
    """
    qualified_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualifiedType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 256,
            "pattern": r"(witsml|resqml|prodml|eml|custom)[1-9]\d\.\w+",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
