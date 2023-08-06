from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.compressibility_kind import CompressibilityKind
from prodml22.reciprocal_pressure_measure import ReciprocalPressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OilCompressibility(ReciprocalPressureMeasure):
    """
    Oil compressibility.

    :ivar kind: The kind of measurement for oil compressibility.
    """
    kind: Optional[CompressibilityKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
