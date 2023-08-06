from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.analysis_line import AnalysisLine
from prodml22.custom_parameter import CustomParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SpecializedAnalysis:
    """This is an analysis not defined by a PTA model but performed on some
    specialized plot.

    It can report using AnyParameter which allows use of any parameter
    as used in the PTA models, or report Custom Parameters. See these
    classes for more information.

    :ivar specialized_analysis_type: The type of specialized analysis.
        Descriptive text. These are not cataloged in the data model.
    :ivar any_parameter: Allows Parameters from the library included in
        the schema to be added to the Specialized Analysis. Type is
        AbstractParameter and the concrete instances are all Parameters.
    :ivar custom_parameter: Allows Custom Parameters to be added to the
        Specialized Analysis. See Custom Parameter for how its
        properties are defined.
    :ivar specialized_xaxis_description: The transform of X axis data
        described textually, for the Specialized Analysis concerned.
    :ivar specialized_yaxis_description: The transform of Y axis data
        described textually, for the Specialized Analysis concerned.
    :ivar analysis_pressure_function: The transformed pressure and
        derivative (contained in referenced Channels) (transformed to
        the trasnform of this specialized analysis) used in this
        analysis. The transforms of Y and X axes are described textually
        in the Specialized [X orY] Axis Description elements.
    :ivar remark: Textual description about the value of this field.
    :ivar analysis_line:
    """
    specialized_analysis_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecializedAnalysisType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    any_parameter: List[AbstractParameter] = field(
        default_factory=list,
        metadata={
            "name": "AnyParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custom_parameter: List[CustomParameter] = field(
        default_factory=list,
        metadata={
            "name": "CustomParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    specialized_xaxis_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecializedXAxisDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    specialized_yaxis_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecializedYAxisDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    analysis_pressure_function: Optional[AbstractPtaPressureData] = field(
        default=None,
        metadata={
            "name": "AnalysisPressureFunction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
