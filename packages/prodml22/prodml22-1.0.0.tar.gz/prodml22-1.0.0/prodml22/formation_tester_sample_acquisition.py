from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition import FluidSampleAcquisition
from prodml22.measured_depth import MeasuredDepth
from prodml22.pressure_measure_ext import PressureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FormationTesterSampleAcquisition(FluidSampleAcquisition):
    """
    Information about the job to take a sample directly from the formation
    using a wireline formation tester (WFT).

    :ivar wellbore:
    :ivar md_top:
    :ivar md_base:
    :ivar sample_container_name:
    :ivar sample_carrier_slot_name: Reference to the WFT station within
        the top-level WFT run data object  where this sample was
        obtained.
    :ivar sample_container_configuration:
    :ivar cushion_pressure:
    :ivar gross_fluid_kind:
    :ivar tool_serial_number:
    :ivar tool_section_name: Reference to the WFT sample within the WFT
        station from where this sample was obtained.
    :ivar flow_test_activity:
    """
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    md_top: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    md_base: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sample_container_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleContainerName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    sample_carrier_slot_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleCarrierSlotName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    sample_container_configuration: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleContainerConfiguration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cushion_pressure: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "CushionPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_fluid_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrossFluidKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    tool_section_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolSectionName",
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
