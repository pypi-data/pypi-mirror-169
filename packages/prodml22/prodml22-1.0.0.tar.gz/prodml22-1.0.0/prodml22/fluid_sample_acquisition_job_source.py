from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSampleAcquisitionJobSource:
    """
    Reference to the fluid sample acquisition within a fluid sample acquisition
    job which acquired this fluid sample.

    :ivar fluid_sample_acquisition_reference: Reference to the fluid
        sample acquisition (by uid) within a fluid sample acquisition
        job (which is referred to as a top-level object) which acquired
        this fluid sample.
    :ivar fluid_sample_acquisition_job_reference:
    """
    fluid_sample_acquisition_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FluidSampleAcquisitionReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    fluid_sample_acquisition_job_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSampleAcquisitionJobReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
