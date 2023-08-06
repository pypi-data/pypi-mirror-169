from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_disposition import AbstractDisposition
from prodml22.disposition_kind import DispositionKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductDisposition(AbstractDisposition):
    """
    Volumes that "left" the reporting entity by one of the disposition methods
    defined in Kind (e.g., flaring, sold, used on site, etc.)

    :ivar kind: The method of disposition. See enum DispositionKind.
    """
    kind: Optional[Union[DispositionKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
