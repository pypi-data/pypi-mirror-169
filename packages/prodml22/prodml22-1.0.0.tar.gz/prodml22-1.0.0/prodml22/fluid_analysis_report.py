from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.data_object_reference import DataObjectReference
from prodml22.report_location import ReportLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidAnalysisReport:
    """
    Fluid analysis report.

    :ivar report_identifier: The identifier of this fluid analysis
        report.
    :ivar report_date: The date of this report.
    :ivar author: The author of this fluid analysis report.
    :ivar analysis_laboratory: The laboratory that provided this fluid
        analysis report.
    :ivar report_document: A reference to the report document, which
        will use the Energistics Attachment Object.
    :ivar report_location:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    report_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportIdentifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    report_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReportDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    analysis_laboratory: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisLaboratory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    report_document: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReportDocument",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    report_location: List[ReportLocation] = field(
        default_factory=list,
        metadata={
            "name": "ReportLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
