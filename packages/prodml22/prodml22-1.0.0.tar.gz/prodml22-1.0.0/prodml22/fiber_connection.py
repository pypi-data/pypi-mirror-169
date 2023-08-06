from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.fiber_common import FiberCommon
from prodml22.fiber_connector_kind import FiberConnectorKind
from prodml22.fiber_end_kind import FiberEndKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberConnection(FiberCommon):
    """
    A connection component within the optical path.

    :ivar connector_type: Specifies whether this is a dry mate or wet
        mate.
    :ivar end_type: Describes whether the fiber end is angle polished or
        flat polished.
    """
    connector_type: Optional[FiberConnectorKind] = field(
        default=None,
        metadata={
            "name": "ConnectorType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    end_type: Optional[FiberEndKind] = field(
        default=None,
        metadata={
            "name": "EndType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
