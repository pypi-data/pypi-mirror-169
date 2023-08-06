from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.data_object_reference import DataObjectReference
from prodml22.interpretation_processing_type import InterpretationProcessingType
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsInterpretationData:
    """
    Header data for a particular collection of interpretation data.

    :ivar facility_mapping: A reference to the facilityMapping to which
        this InterpretationData relates. The facility mapping relates a
        length of fiber to a corresponding length of a facility
        (probably a wellbore or pipeline). The facilityMapping also
        contains the datum from which the InterpretedData is indexed.
    :ivar sampling_interval: The difference in fiber distance between
        consecutive temperature sample points in a single temperature
        trace.
    :ivar bad_flag: Indicates whether or not the interpretation log
        contains bad data. This flag allows you to keep bad data  (so at
        least you know that something was generated/acquired) and filter
        it out when doing relevant data operations.
    :ivar creation_start_time: Time when the interpretation log data was
        generated.
    :ivar interpretation_processing_type: Indicates what type of post-
        processing technique was used to generate this interpretation
        log. Enum list. The meaning is that this process was applied to
        the InterpretedData referenced by the parentInterpretationID.
    :ivar index_mnemonic: The mnemonic of the channel in the
        InterpretedData that represents the index to the data (expected
        to be a length along the facility (e.g., wellbore, pipeline)
        being measured.
    :ivar point_count: The number of rows in this interpreted data
        object. Each row or "point" represents a measurement along the
        fiber.
    :ivar channel_set: Pointer to a ChannelSet containing the comma-
        delimited list of mnemonics and units, and channel data
        representing the interpretation data. BUSINESS RULE: The
        mnemonics and the units must follow a strict order. The mnemonic
        list must be in this order: facilityDistance,
        adjustedTemperature The unit list must be one of the following:
        - m,degC - ft,degF
    :ivar comment: A descriptive remark about the interpretation log.
    :ivar measurement_reference: Mandatory element indicating that the
        referenced MeasuredTraceSet object is the raw trace data from
        which this InterpretedData is derived. This is needed so that
        any InterpretedData can be related to the raw measurement from
        which it is derived.
    :ivar parent_interpretation_reference: Optional element indicating
        that the referenced InterpretedData object is the parent from
        which this InterpretedData is derived. Example, this instance
        may be derived from a parent by the data having been
        temperature-shifted to match an external data source. The
        element InterpretationProcessingType is provided to record which
        type of operation was performed on the parent data to obtain
        this instance of data.
    :ivar uid: Unique identifier of this object.
    """
    facility_mapping: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
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
    bad_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BadFlag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    creation_start_time: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CreationStartTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    interpretation_processing_type: Optional[InterpretationProcessingType] = field(
        default=None,
        metadata={
            "name": "InterpretationProcessingType",
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
    measurement_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    parent_interpretation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentInterpretationReference",
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
