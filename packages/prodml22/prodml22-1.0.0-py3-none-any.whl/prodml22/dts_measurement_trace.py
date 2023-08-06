from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.frequency_measure import FrequencyMeasure
from prodml22.length_measure import LengthMeasure
from prodml22.trace_processing_type import TraceProcessingType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsMeasurementTrace:
    """
    Header data for raw (measured) traces collections.

    :ivar trace_processing_type: Denotes whether the trace was stored as
        acquired by the measurement device or recalibrated in any way.
    :ivar sampling_interval: The difference in fiber distance between
        consecutive temperature sample points in a single temperature
        trace.
    :ivar index_mnemonic: The mnemonic of the channel in the
        MeasuredTraceSet that represents the index to the data (expected
        to be a length along the facility (e.g., wellbore, pipeline)
        being measured.
    :ivar point_count: The number of rows in this interpreted data
        object. Each row or "point" represents a measurement along the
        fiber.
    :ivar frequency_rayleigh1: Frequency reference for Rayleigh 1
        measurement.
    :ivar frequency_rayleigh2: Frequency reference for Rayleigh 2
        measurement.
    :ivar channel_set: Pointer to a ChannelSet containing the comma-
        delimited list of mnemonics and units, and channel data
        representing the measurement trace. BUSINESS RULE: The mnemonics
        and the units must follow a strict order. The mnemonic list must
        be in this order: fiberDistance, antistokes, stokes,
        reverseAntiStokes, reverseStokes, rayleigh1, rayleigh2,
        brillouinfrequency, loss, lossRatio, cumulativeExcessLoss,
        frequencyQualityMeasure, measurementUncertainty,
        brillouinAmplitude, opticalPathTemperature,
        uncalibratedTemperature1, uncalibratedTemperature2 The unit list
        must be one of the following: - m, mW, mW, mW, mW, mW, mW, GHz,
        dB/Km, dB/Km, dB, dimensionless, degC, mW, degC, DegC, degC -
        ft, mW, mW, mW, mW,mW, mW, GHz, dB/Km, dB/Km,dB, dimensionless,
        degF, mW, degF, degF, degF
    :ivar comment: A descriptive remark about the measured trace set.
    :ivar parent_measurement_reference: Where this dtsMeasuredTraceSet
        was derived from a parent dtsMeasuredTraceSet (having been
        recalibrated for example), the parent dtsMeasuredTraceSet can be
        indicated by referencing its UID with this element.
    :ivar uid: Unique identifier of this object.
    """
    trace_processing_type: Optional[TraceProcessingType] = field(
        default=None,
        metadata={
            "name": "TraceProcessingType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    sampling_interval: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SamplingInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    index_mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexMnemonic",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    point_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PointCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    frequency_rayleigh1: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "FrequencyRayleigh1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    frequency_rayleigh2: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "FrequencyRayleigh2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    channel_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    parent_measurement_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentMeasurementReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
