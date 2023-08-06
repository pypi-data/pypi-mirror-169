from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RatioDpSkinToTotalDrawdown(AbstractParameter):
    """The ratio of the DeltaPressureTotalSkin to the total drawdown pressure.

    Indicates the fraction of the total pressure drawdown due to
    completion effects such as convergence, damage, etc.  The remaining
    pressure drop is due to radial flow in the reservoir.
    """
    abbreviation: str = field(
        init=False,
        default="Ratio dP Skin To Total",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    value: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
