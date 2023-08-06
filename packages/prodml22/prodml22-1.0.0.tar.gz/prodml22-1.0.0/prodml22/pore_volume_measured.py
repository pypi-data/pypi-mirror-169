from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PoreVolumeMeasured(AbstractParameter):
    """In a closed reservoir model, the Pore Volume measured.

    This is to be taken to mean that the analysis yielded a measurement,
    as opposed to the RadiusOfInvestigation or PoreVolumeOfInvestigation
    Parameters which are taken to mean the estimates for these
    parameters derived from diffuse flow theory, but not necessarily
    measured.
    """
    abbreviation: str = field(
        init=False,
        default="PVmeas",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
