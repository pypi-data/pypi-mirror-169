from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_flow_test_data import AbstractFlowTestData
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_measure import LengthMeasure
from prodml22.reference_point_kind import ReferencePointKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractPtaPressureData(AbstractFlowTestData):
    """
    The abstract class of pressure data from which all flow test data
    components inherit.

    :ivar pressure_channel: A channel is a series of individual data
        points. A channel is comparable to a log curve; more generally,
        it is comparable to a tag in a process historian. Channels
        organize their data points according to one or more channel
        indexes, in this case, pressure.
    :ivar pressure_derivative_channel: A channel is a series of
        individual data points. A channel is comparable to a log curve;
        more generally, it is comparable to a tag in a process
        historian. Channels organize their data points according to one
        or more channel indexes, in this case, derived from another
        pressure channel.
    :ivar pressure_reference_depth: A depth relative to a base or datum.
    :ivar datum: The datum (which is an enum of type Datum in WITSML)
        from which the element PressureReferenceDepth is measured.
    """
    pressure_channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PressureChannel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    pressure_derivative_channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PressureDerivativeChannel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pressure_reference_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PressureReferenceDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    datum: Optional[ReferencePointKind] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
