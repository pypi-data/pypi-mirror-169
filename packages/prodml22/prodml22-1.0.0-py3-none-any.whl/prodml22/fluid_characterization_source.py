from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationSource:
    """
    Fluid characterization source.

    :ivar fluid_analysis_test_reference: A reference to a fluid analysis
        test which was used as source data for this fluid
        characterization.
    :ivar fluid_analysis:
    """
    fluid_analysis_test_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FluidAnalysisTestReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    fluid_analysis: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidAnalysis",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
