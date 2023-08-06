from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DownholeSampleAcquisition(FluidSampleAcquisition):
    """
    Additional information required for a sample acquired down hole.

    :ivar wellbore: A reference to the wellbore (a WITSML data object)
        where this downhole sample was taken.
    :ivar wellbore_completion: A reference to the wellbore completion
        (WITSML data object) where this sample was taken.
    :ivar sampling_run: The sampling run number for this downhole sample
        acquisition.
    :ivar top_md: The top MD for the interval where this downhole sample
        was taken.
    :ivar base_md: The base MD for the interval where this downhole
        sample was taken.
    :ivar tool_serial_number:
    :ivar tool_kind: The kind of tool used to acquire the downhole
        sample.
    :ivar flow_test_activity:
    """
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    wellbore_completion: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellboreCompletion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sampling_run: Optional[int] = field(
        default=None,
        metadata={
            "name": "SamplingRun",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    top_md: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TopMD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    base_md: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BaseMD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tool_serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolSerialNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    tool_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    flow_test_activity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
