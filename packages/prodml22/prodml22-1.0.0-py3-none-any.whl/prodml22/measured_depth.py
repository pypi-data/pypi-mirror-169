from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_measure_ext import LengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MeasuredDepth:
    """A measured depth coordinate in a wellbore.

    Positive moving from the reference datum toward the bottomhole. All
    coordinates with the same datum (and same UOM) can be considered to
    be in the same coordinate reference system (CRS) and are thus
    directly comparable.

    :ivar measured_depth:
    :ivar datum: The datum the measured depth is referenced to. Required
        when there is no default MD datum associated with the data
        object this is used in.
    """
    measured_depth: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "MeasuredDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
