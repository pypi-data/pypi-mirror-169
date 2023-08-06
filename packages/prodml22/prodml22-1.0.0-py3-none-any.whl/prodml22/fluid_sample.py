from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_sample_acquisition_job_source import FluidSampleAcquisitionJobSource
from prodml22.fluid_sample_chain_of_custody_event import FluidSampleChainOfCustodyEvent
from prodml22.fluid_sample_kind import FluidSampleKind
from prodml22.sample_recombination_specification import SampleRecombinationSpecification

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSample(AbstractObject):
    """
    The fluid sample.

    :ivar sample_kind: The kind of sample. Enum.  See fluid sample kind.
    :ivar rock_fluid_unit_interpretation: Reference to a
        RockFluidUnitInterpretation (a RESQML class).
    :ivar representative: Boolean to state whether the sample is
        representative or not.
    :ivar sample_disposition: The sample disposition, if any.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_sample_chain_of_custody_event: Fluid sample custody
        history event.
    :ivar original_sample_container:
    :ivar fluid_system:
    :ivar fluid_sample_acquisition_job_source: Reference to the fluid
        sample acquisition within a fluid sample acquisition job which
        acquired this fluid sample.
    :ivar sample_recombination_specification: A sample recombination.
    :ivar associated_fluid_sample:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    sample_kind: Optional[Union[FluidSampleKind, str]] = field(
        default=None,
        metadata={
            "name": "SampleKind",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    rock_fluid_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RockFluidUnitInterpretation",
            "type": "Element",
        }
    )
    representative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Representative",
            "type": "Element",
        }
    )
    sample_disposition: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleDisposition",
            "type": "Element",
            "max_length": 64,
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
    fluid_sample_chain_of_custody_event: List[FluidSampleChainOfCustodyEvent] = field(
        default_factory=list,
        metadata={
            "name": "FluidSampleChainOfCustodyEvent",
            "type": "Element",
        }
    )
    original_sample_container: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OriginalSampleContainer",
            "type": "Element",
        }
    )
    fluid_system: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSystem",
            "type": "Element",
        }
    )
    fluid_sample_acquisition_job_source: Optional[FluidSampleAcquisitionJobSource] = field(
        default=None,
        metadata={
            "name": "FluidSampleAcquisitionJobSource",
            "type": "Element",
        }
    )
    sample_recombination_specification: Optional[SampleRecombinationSpecification] = field(
        default=None,
        metadata={
            "name": "SampleRecombinationSpecification",
            "type": "Element",
        }
    )
    associated_fluid_sample: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedFluidSample",
            "type": "Element",
        }
    )
