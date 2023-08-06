from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fluid_component import AbstractFluidComponent
from prodml22.mass_per_mass_measure import MassPerMassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FormationWater(AbstractFluidComponent):
    """
    The water in the formation.

    :ivar specific_gravity: Specific gravity.
    :ivar salinity: Salinity level.
    :ivar remark: Remarks and comments about this data item.
    """
    specific_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "SpecificGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    salinity: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Salinity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
