from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_temperature_pressure import AbstractTemperaturePressure
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_analysis_report import FluidAnalysisReport
from prodml22.fluid_component_catalog import FluidComponentCatalog
from prodml22.sample_contaminant import SampleContaminant
from prodml22.sample_quality import SampleQuality

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidAnalysis(AbstractObject):
    """
    Fluid analysis.

    :ivar request_date: The date the fluid analysis was requested of a
        lab services provider (eg the date of a contract or purchase
        order)."
    :ivar client:
    :ivar start_time:
    :ivar end_time:
    :ivar analysis_description: The description about the analysis.
    :ivar analysis_purpose: The purpose of this analysis.
    :ivar analysis_site: The location site of the analysis.
    :ivar lab_contact: The name of the analyst or user who is
        responsible for the results.
    :ivar standard_conditions: The standard temperature and pressure
        used for the representation of this fluid analysis.
    :ivar analysis_quality: Enum for the quality of this analysis.  See
        sample quality.
    :ivar fluid_component_catalog: The fluid component catalog for this
        fluid analysis.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_analysis_report: Fluid analysis report.
    :ivar sample_contaminant: Sample contaminant information.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    request_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RequestDate",
            "type": "Element",
        }
    )
    client: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Client",
            "type": "Element",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    analysis_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisDescription",
            "type": "Element",
            "max_length": 2000,
        }
    )
    analysis_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisPurpose",
            "type": "Element",
            "max_length": 2000,
        }
    )
    analysis_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisSite",
            "type": "Element",
            "max_length": 2000,
        }
    )
    lab_contact: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LabContact",
            "type": "Element",
        }
    )
    standard_conditions: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "StandardConditions",
            "type": "Element",
            "required": True,
        }
    )
    analysis_quality: Optional[SampleQuality] = field(
        default=None,
        metadata={
            "name": "AnalysisQuality",
            "type": "Element",
            "required": True,
        }
    )
    fluid_component_catalog: Optional[FluidComponentCatalog] = field(
        default=None,
        metadata={
            "name": "FluidComponentCatalog",
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
    fluid_analysis_report: List[FluidAnalysisReport] = field(
        default_factory=list,
        metadata={
            "name": "FluidAnalysisReport",
            "type": "Element",
        }
    )
    sample_contaminant: List[SampleContaminant] = field(
        default_factory=list,
        metadata={
            "name": "SampleContaminant",
            "type": "Element",
        }
    )
