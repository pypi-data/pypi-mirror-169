from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.analysis_line import AnalysisLine
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.log_log_pressure_transform import LogLogPressureTransform
from prodml22.log_log_time_transform import LogLogTimeTransform

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LogLogAnalysis:
    """
    Contains the result data needed to plot or overlay measured data and
    simulated data for PTA in a standard log-log axes plot.

    :ivar analysis_pressure: The transformed pressure and derivative
        (contained in referenced Channels) (to log-log transform) used
        in this log-log analysis.
    :ivar log_log_time_data_transform: Describes the type of transform
        applied to the time axis of the log log plot. Enum. Options:
        delta-time (ie, no tranform) and various superposition time
        functions (ie, time transformed to represent equivalent drawdown
        time using superposition).
    :ivar log_log_pressure_transform: Describes the type of transform
        applied to the pressure axis of the log log plot. Enum. Options:
        pressure, and various pressure/flowrate functions.
    :ivar derivative_smoothing_factor_l: The smoothing factor for the
        derivative curve. Common symbolized as L.
    :ivar remark: Textual description about the value of this field.
    :ivar analysis_line:
    """
    analysis_pressure: Optional[AbstractPtaPressureData] = field(
        default=None,
        metadata={
            "name": "AnalysisPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    log_log_time_data_transform: Optional[LogLogTimeTransform] = field(
        default=None,
        metadata={
            "name": "LogLogTimeDataTransform",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    log_log_pressure_transform: Optional[LogLogPressureTransform] = field(
        default=None,
        metadata={
            "name": "LogLogPressureTransform",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    derivative_smoothing_factor_l: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "DerivativeSmoothingFactorL",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    analysis_line: List[AnalysisLine] = field(
        default_factory=list,
        metadata={
            "name": "AnalysisLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
