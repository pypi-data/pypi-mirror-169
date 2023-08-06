from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.area_measure import AreaMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DrainageAreaMeasured(AbstractParameter):
    """In a closed reservoir model, the Drainage Area measured.

    This is to be taken to mean that the analysis yielded a measurement,
    as opposed to the RadiusOfInvestigation or PoreVolumeOfInvestigation
    Parameters which are taken to mean the estimates for these
    parameters derived from diffuse flow theory, but not necessarily
    measured.
    """
    abbreviation: str = field(
        init=False,
        default="A",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    area: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
