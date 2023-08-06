from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class VerticalAnisotropyKvToKr(AbstractParameter):
    """The Vertical Anisotropy of permeability, K(vertical)/K(radial).

    K(radial) is the effective horizontal permeability, which in
    anisotropic horizontal permeability equals square root (Kx^2+Ky^2).
    Optional since many models do not account for this parameter. It
    will be mandatory in some models however, e.g. limited entry or
    horizontal wellbore models.
    """
    abbreviation: str = field(
        init=False,
        default="kvTokr",
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
