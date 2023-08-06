from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LeakSkin(AbstractParameter):
    """In Spivey (a) Packer and (c) Fissure models of wellbore storage, the Leak Skin controls the pressure communication through the packer (a), or between the wellbore and the high permeability region (b - second application of model a), or between the high permeability channel/fissures and the reservoir (c). In  case c, the usual Skin parameter characterizes the pressure communication between the wellbore and the high permeability channel/fissures."""
    abbreviation: str = field(
        init=False,
        default="Sl",
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
