from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AnalysisLine:
    """
    Describes a straight line on any analysis plot.

    :ivar line_name: The name of the line.
    :ivar slope: The slope of the line.
    :ivar intercept: The intercept of the line.
    :ivar remark: Textual description about the value of this field.
    """
    line_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "Slope",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    intercept: Optional[float] = field(
        default=None,
        metadata={
            "name": "Intercept",
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
