from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.osdulineage_relationship_kind import OsdulineageRelationshipKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class OsdulineageAssertion:
    """Defines relationships with other objects (any kind of Resource) upon
    which this work product component depends.

    The assertion is directed only from the asserting WPC to ancestor
    objects, not children.  It should not be used to refer to files or
    artefacts within the WPC -- the association within the WPC is
    sufficient and Artefacts are actually children of the main WPC file.

    :ivar id: The OSDU identifier of the dependent object.
    :ivar lineage_relationship_kind:
    """
    class Meta:
        name = "OSDULineageAssertion"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 256,
        }
    )
    lineage_relationship_kind: Optional[OsdulineageRelationshipKind] = field(
        default=None,
        metadata={
            "name": "LineageRelationshipKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
