from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_rate_history import AbstractRateHistory
from prodml22.time_measure import TimeMeasure
from prodml22.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SingleFlowrateData(AbstractRateHistory):
    """
    Contains the data for a simple representation of flowrate comprising a
    single rate and a flowing time.

    :ivar effective_producing_time_used: If a single flowrate and
        effective producing time was used, this is the effective
        producing time used in the analysis. Usually abbreviated Tpeff.
    :ivar single_flowrate: If a single flowrate and effective producing
        time was used, this is the single flowrate value used in the
        analysis.
    """
    effective_producing_time_used: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "EffectiveProducingTimeUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    single_flowrate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "SingleFlowrate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
