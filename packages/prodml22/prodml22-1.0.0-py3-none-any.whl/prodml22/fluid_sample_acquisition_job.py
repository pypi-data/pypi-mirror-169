from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSampleAcquisitionJob(AbstractObject):
    """
    Information about the job that results in acquiring a fluid sample.

    :ivar client:
    :ivar start_time: The date when fluid acquisition started.
    :ivar end_time:
    :ivar flow_test_job:
    :ivar fluid_sample_acquisition: Information common to any fluid
        sample taken. Additional details can be captured in related data
        object depending on the where the sample was taken, for example:
        downhole, separator, wellhead, of the formation using a wireline
        formation tester (WFT). If the tool used to capture samples has
        multiple containers, each container has a separate instance of
        fluid sample acquisition.
    :ivar fluid_system:
    :ivar service_company:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    client: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Client",
            "type": "Element",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flow_test_job: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowTestJob",
            "type": "Element",
        }
    )
    fluid_sample_acquisition: List[FluidSampleAcquisition] = field(
        default_factory=list,
        metadata={
            "name": "FluidSampleAcquisition",
            "type": "Element",
        }
    )
    fluid_system: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSystem",
            "type": "Element",
            "required": True,
        }
    )
    service_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
        }
    )
