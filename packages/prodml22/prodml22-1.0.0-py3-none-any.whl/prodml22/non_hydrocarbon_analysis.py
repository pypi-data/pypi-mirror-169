from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_analysis import FluidAnalysis
from prodml22.non_hydrocarbon_test import NonHydrocarbonTest

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NonHydrocarbonAnalysis(FluidAnalysis):
    fluid_sample: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flow_test_activity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    non_hydrocarbon_test: List[NonHydrocarbonTest] = field(
        default_factory=list,
        metadata={
            "name": "NonHydrocarbonTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
