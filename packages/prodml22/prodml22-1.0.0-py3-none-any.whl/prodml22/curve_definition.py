from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.measure_class import MeasureType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CurveDefinition:
    """
    The definition of a curve.

    :ivar order: The order of the value in the index or data tuple. If
        isIndex is true, this is the order of the (independent) index
        element. If isIndex is false, this is the order of the
        (dependent) value element.
    :ivar parameter: The name of the variable in this curve.
    :ivar is_index: True (equal "1" or "true") indicates that this is an
        independent variable in this curve. At least one column column
        should be flagged as independent.
    :ivar measure_class: The measure class of the variable. This defines
        which units of measure are valid for the value.
    :ivar unit: The unit of measure of the variable. The unit of measure
        must match a unit allowed by the measure class.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    parameter: Optional[str] = field(
        default=None,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    is_index: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 32,
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
