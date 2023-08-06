from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_flow_test_data import AbstractFlowTestData
from prodml22.abstract_object import AbstractObject
from prodml22.data_conditioning import DataConditioning
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PtaDataPreProcess(AbstractObject):
    """
    Superclass defining data acquisition for the flow test, input and pre-
    processing data.

    :ivar flow_test_activity: A reference, using data object reference,
        to a FlowTestActivity data-object containing the measurement
        data which this PreProcess applies to.
    :ivar flow_test_measurement_set_ref: A reference, using uid, to the
        Flow Test Measurement Set within the Flow Test Activity data-
        object containing the measurement data which this PreProcess
        applies to.
    :ivar input_data: One or more input channels being pre-processed in
        this PreProcess.
    :ivar pre_processed_data: The data (in a Channel) which is the
        output of this PreProcess.
    :ivar data_conditioning: Type of data conditioning that may describe
        multiple preprocessing steps
    :ivar remark: Textual description about the value of this field.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    flow_test_activity: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    flow_test_measurement_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowTestMeasurementSetRef",
            "type": "Element",
            "max_length": 64,
        }
    )
    input_data: List[AbstractFlowTestData] = field(
        default_factory=list,
        metadata={
            "name": "InputData",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    pre_processed_data: Optional[AbstractFlowTestData] = field(
        default=None,
        metadata={
            "name": "PreProcessedData",
            "type": "Element",
            "required": True,
        }
    )
    data_conditioning: List[Union[DataConditioning, str]] = field(
        default_factory=list,
        metadata={
            "name": "DataConditioning",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_length": 2000,
        }
    )
