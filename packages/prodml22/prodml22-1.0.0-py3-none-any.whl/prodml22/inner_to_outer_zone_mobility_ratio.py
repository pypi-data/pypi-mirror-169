from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InnerToOuterZoneMobilityRatio(AbstractParameter):
    """
    In a Radial or Linear Composite model, the mobility
    (permeability/viscosity) ratio of inner zone/outer zone.
    """
    abbreviation: str = field(
        init=False,
        default="M",
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
