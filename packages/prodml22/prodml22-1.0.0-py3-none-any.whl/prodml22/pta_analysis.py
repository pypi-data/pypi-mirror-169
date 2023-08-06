from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_analysis import AbstractAnalysis
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.abstract_rate_history import AbstractRateHistory
from prodml22.log_log_analysis import LogLogAnalysis
from prodml22.output_pressure_data import OutputPressureData
from prodml22.pressure_measure import PressureMeasure
from prodml22.pressure_per_time_measure import PressurePerTimeMeasure
from prodml22.specialized_analysis import SpecializedAnalysis

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PtaAnalysis(AbstractAnalysis):
    """Contains the input and output (simulated) data needed for analysis of
    pressure (PTA) (ie where flowrate is the boundary condition).

    Can contain log log plots of the data. Can contain Specialized
    Analyses and their plots of the data.  The Model data itself is
    contained in the WellboreModel and LayerModel elements of the
    TestLocationAnalysis.

    :ivar initial_pressure_p0_for_impulse_test: Only required for
        Impulse type tests: P0 (Pressure at time zero), the instant
        pressure at the start of the test.
    :ivar input_pressure: The pressure (in a Channel) which is being
        analysed in this PTA.
    :ivar simulated_pressure: Reference to the UID of the Output
        Pressure Data from this Analysis. This will be a simulated
        response. For Test Design this will be the only pressure time
        series present.
    :ivar simulated_pressure_gauge_noise: Optional element to report the
        addition of noise to the pressure signal for Test Design
        purposes.  The value is equal to the magnitude of the random
        noise added. Ie, if value is "x" then random noise distributed
        within +/-x has been added.
    :ivar simulated_pressure_gauge_resolution: Optional element to
        report the addition of gauge resolution to the pressure signal
        for Test Design purposes.  The value is equal to the magnitude
        of the gauge resolution.
    :ivar simulated_pressure_gauge_drift: Optional element to report the
        addition of gauge drift to the pressure signal for Test Design
        purposes.  The value is equal to the magnitude of the gauge
        drift in terms of units of pressure per unit of time, applied
        across the time duration of this Result. A negative sign means
        the drift is negative, ie the gauge is drifting to read a less
        positive value than the correct value as time passes.
    :ivar measured_log_log_data:
    :ivar simulated_log_log_data:
    :ivar rate_history: Choice between full rate history (time series)
        and single flowrate and time (Q &amp; tp).
    :ivar specialized_analysis:
    """
    initial_pressure_p0_for_impulse_test: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "InitialPressureP0ForImpulseTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    input_pressure: Optional[AbstractPtaPressureData] = field(
        default=None,
        metadata={
            "name": "InputPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    simulated_pressure: Optional[OutputPressureData] = field(
        default=None,
        metadata={
            "name": "SimulatedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    simulated_pressure_gauge_noise: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "SimulatedPressureGaugeNoise",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    simulated_pressure_gauge_resolution: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "SimulatedPressureGaugeResolution",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    simulated_pressure_gauge_drift: Optional[PressurePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "SimulatedPressureGaugeDrift",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_log_log_data: Optional[LogLogAnalysis] = field(
        default=None,
        metadata={
            "name": "MeasuredLogLogData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    simulated_log_log_data: Optional[LogLogAnalysis] = field(
        default=None,
        metadata={
            "name": "SimulatedLogLogData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    rate_history: Optional[AbstractRateHistory] = field(
        default=None,
        metadata={
            "name": "RateHistory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    specialized_analysis: List[SpecializedAnalysis] = field(
        default_factory=list,
        metadata={
            "name": "SpecializedAnalysis",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
