from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_measure import LengthMeasure
from prodml22.length_per_length_measure import LengthPerLengthMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumePortDifference:
    """
    Product Volume port differential characteristics.

    :ivar port_reference: A port on the other end of an internal
        connection. This should always be specified if a product flow
        network is being referenced by this report. If this is not
        specified then there is an assumption that there is only one
        other port for the unit. For example, if this end of the
        connection represents an inlet port then the implied other end
        is the outlet port for the unit.
    :ivar pres_diff: The differential pressure between the ports.
    :ivar temp_diff: The differential temperature between the ports.
    :ivar choke_size: The size of the choke. This characterizes the
        overall unit with respect to the flow restriction between the
        ports. The restriction might be implemented using a valve or an
        actual choke.
    :ivar choke_relative: The relative size of the choke restriction.
        This characterizes the overall unit with respect to the flow
        restriction between the ports. The restriction might be
        implemented using a valve or an actual choke.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    port_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    pres_diff: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresDiff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    temp_diff: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempDiff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    choke_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChokeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    choke_relative: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChokeRelative",
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
