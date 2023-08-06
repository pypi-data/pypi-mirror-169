from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_deconvolution_output import AbstractDeconvolutionOutput
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.data_object_reference import DataObjectReference
from prodml22.deconvolved_flow_data import DeconvolvedFlowData
from prodml22.deconvolved_pressure_data import DeconvolvedPressureData
from prodml22.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PtaDeconvolution(AbstractObject):
    """
    Superclass of deconvolution pressure and flowrate measurements, test and
    method information.

    :ivar flow_test_activity: A reference, using data object reference,
        to a FlowTestActivity data-object containing the measurement
        data which this Deconvolution applies to.
    :ivar flow_test_measurement_set_ref: A reference, using uid, to the
        Flow Test Measurement Set within the Flow Test Activity data-
        object containing the measurement data which this Deconvolution
        applies to.
    :ivar flow_test_period_ref: Reference to the test periods which are
        included in the input to the deconvolution.
    :ivar method_name: The name of the method for this deconvolution.
    :ivar initial_pressure: The initial reservoir pressure. Note that
        this may be in input to, or output from, the deconvolution
        algorithm.
    :ivar input_pressure: The pressure data (in a Channel) which is
        being deconvolved in this Deconvolution.
    :ivar input_flowrate: The flow data (in a Channel) which is being
        deconvolved in this Deconvolution.
    :ivar reconstructed_pressure: The reconstructed pressure data (in a
        Channel) which is the output of this Deconvolution.
    :ivar reconstructed_flowrate: The reconstructed flow rate data (in a
        Channel) which is the output of this Deconvolution.
    :ivar remark: Textual description about the value of this field.
    :ivar deconvolution_output:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    flow_test_activity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "required": True,
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
    flow_test_period_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FlowTestPeriodRef",
            "type": "Element",
            "max_length": 64,
        }
    )
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    initial_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "InitialPressure",
            "type": "Element",
            "required": True,
        }
    )
    input_pressure: Optional[AbstractPtaPressureData] = field(
        default=None,
        metadata={
            "name": "InputPressure",
            "type": "Element",
            "required": True,
        }
    )
    input_flowrate: Optional[AbstractPtaFlowData] = field(
        default=None,
        metadata={
            "name": "InputFlowrate",
            "type": "Element",
            "required": True,
        }
    )
    reconstructed_pressure: Optional[DeconvolvedPressureData] = field(
        default=None,
        metadata={
            "name": "ReconstructedPressure",
            "type": "Element",
        }
    )
    reconstructed_flowrate: Optional[DeconvolvedFlowData] = field(
        default=None,
        metadata={
            "name": "ReconstructedFlowrate",
            "type": "Element",
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
    deconvolution_output: List[AbstractDeconvolutionOutput] = field(
        default_factory=list,
        metadata={
            "name": "DeconvolutionOutput",
            "type": "Element",
            "min_occurs": 1,
        }
    )
