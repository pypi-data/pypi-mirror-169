from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_cable import AbstractCable
from prodml22.permanent_cable_installation_kind import PermanentCableInstallationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PermanentCable(AbstractCable):
    """
    Information on the type of permanent conveyance used by the optical path.

    :ivar permanent_cable_installation_type: Enum. For permanent
        conveyance option, the type of conveyance. Example: clamped to
        tubular.
    :ivar comment: Comment about the intervention conveyance.
    """
    permanent_cable_installation_type: Optional[PermanentCableInstallationKind] = field(
        default=None,
        metadata={
            "name": "PermanentCableInstallationType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
