from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_measure_data import AbstractMeasureData
from prodml22.value_status import ValueStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class GeneralQualifiedMeasure(AbstractMeasureData):
    """A measure which may have a quality status.

    The measure class (e.g., length) must be defined within the context
    of the usage of this type (e.g., in another element). This should
    not be used if the measure class will always be the same thing. If
    the 'status' attribute is absent and the value is not "NaN", the
    data value can be assumed to be good with no restrictions.

    :ivar status: An indicator of the quality of the value.
    :ivar component_reference: The kind of the value component. For
        example, "X" in a tuple of X and Y.
    :ivar uom: The unit of measure for the value. This value must
        conform to the values allowed by the measure class.
    """
    status: Optional[ValueStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        }
    )
