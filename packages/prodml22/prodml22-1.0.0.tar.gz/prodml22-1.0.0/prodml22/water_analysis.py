from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_analysis import FluidAnalysis
from prodml22.sample_integrity_and_preparation import SampleIntegrityAndPreparation
from prodml22.water_analysis_test import WaterAnalysisTest
from prodml22.water_sample_component import WaterSampleComponent

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaterAnalysis(FluidAnalysis):
    """
    A collection of any one or more fluid analyses on water.

    :ivar sample_integrity_and_preparation:
    :ivar water_analysis_test: Water analysis test.
    :ivar water_sample_component:
    :ivar fluid_sample:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    sample_integrity_and_preparation: Optional[SampleIntegrityAndPreparation] = field(
        default=None,
        metadata={
            "name": "SampleIntegrityAndPreparation",
            "type": "Element",
        }
    )
    water_analysis_test: List[WaterAnalysisTest] = field(
        default_factory=list,
        metadata={
            "name": "WaterAnalysisTest",
            "type": "Element",
        }
    )
    water_sample_component: List[WaterSampleComponent] = field(
        default_factory=list,
        metadata={
            "name": "WaterSampleComponent",
            "type": "Element",
        }
    )
    fluid_sample: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSample",
            "type": "Element",
            "required": True,
        }
    )
