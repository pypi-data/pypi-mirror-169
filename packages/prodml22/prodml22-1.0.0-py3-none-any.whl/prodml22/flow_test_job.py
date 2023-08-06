from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlowTestJob(AbstractObject):
    """Operational data regarding flow test. Links to the following (of which
    there can be multiple):

    - Flow Test Activity
    - PressureTransientAnalysis
    - PtaDataPreProcess
    - PtaDeconvolution
    It can also link to one Fluid Sample Acquisition Job.

    :ivar client:
    :ivar service_company:
    :ivar start_time:
    :ivar fluid_sample_acquisition_job:
    :ivar pta_data_pre_process: Superclass defining data acquisition for
        the flow test, input and pre-processing data
    :ivar flow_test_activity: Superclass of possible flow test
        activities: drill stem, production transient, interwell, and
        others.
    :ivar pta_deconvolution: Superclass of deconvolution pressure and
        flowrate measurements, test and method information.
    :ivar pressure_transient_analysis: Contains the data about the
        analysis and the model used, in a PTA Analysis.  An Analysis may
        be a pressure transient (PTA), rate transient (RTA) or Test
        Design, depending on which data is supplied. This object
        contains common parameters. The Analysis has one or more Test
        Location Analysis elements and each reports the model details
        for one Test Location.
    :ivar end_time:
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
    service_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
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
    fluid_sample_acquisition_job: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSampleAcquisitionJob",
            "type": "Element",
        }
    )
    pta_data_pre_process: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "PtaDataPreProcess",
            "type": "Element",
        }
    )
    flow_test_activity: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
        }
    )
    pta_deconvolution: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "PtaDeconvolution",
            "type": "Element",
        }
    )
    pressure_transient_analysis: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "PressureTransientAnalysis",
            "type": "Element",
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
