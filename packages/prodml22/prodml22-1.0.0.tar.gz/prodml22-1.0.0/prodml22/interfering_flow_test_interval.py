from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.output_pressure_data import OutputPressureData

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterferingFlowTestInterval:
    """
    Measurements pertaining to the interfering flow, in the case of an
    interference test.

    :ivar flow_test_measurement_set_ref: A reference (using uid) to the
        flow test measurement set which contains the data concerning the
        interfering flow, in the case of an interference test. (This
        other flow test measurement set will be in the same Flow Test
        Activity top level object and will contain the location, flow
        rates etc of the intefering flow).
    :ivar interfering_flowrate_ref: A reference (using uid) to the flow
        rate which is the measurement of the interfering flow, in the
        case of an interference test.
    :ivar test_period_ref: A reference (using uid) to the test period(s)
        whose effect the interfering flow is being allowed for, in the
        case of an interference test. If unspecified, it should be
        assumed that all test periods can potentially give rise to an
        interference effect.
    :ivar simulated_interference_pressure: The simulated interference
        pressure (which will be at the observation interval), in the
        case of an interference test.
    :ivar simulated_interference_pressure_removed: A flag to indicate if
        the Simulated Interference Pressure for this intefering flow
        interval, has been removed from the measured data. If true, then
        the corrected measured data should be analysable without having
        to consider the intererence effect further.
    :ivar uid: Unique identifier for this instance of the object.
    """
    flow_test_measurement_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlowTestMeasurementSetRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    interfering_flowrate_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterferingFlowrateRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    test_period_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestPeriodRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    simulated_interference_pressure: Optional[OutputPressureData] = field(
        default=None,
        metadata={
            "name": "SimulatedInterferencePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    simulated_interference_pressure_removed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SimulatedInterferencePressureRemoved",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
