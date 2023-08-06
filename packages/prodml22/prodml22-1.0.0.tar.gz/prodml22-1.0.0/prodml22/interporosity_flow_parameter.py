from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterporosityFlowParameter(AbstractParameter):
    """The dimensionless interporosity flow parameter, known as Lambda.

    In dual porosity, represents the ability of the matrix to flow into
    the fissure network. In dual permeability or other multi-layer
    cases, represents the ability of flow to move from one layer to
    another.
    """
    abbreviation: str = field(
        init=False,
        default="Lambda",
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
