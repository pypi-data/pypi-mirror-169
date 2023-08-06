from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.length_measure import LengthMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellFlowingCondition:
    """
    Describes key conditions of the flowing well during a production well test.

    :ivar choke_orifice_size: The choke diameter.
    :ivar bottom_hole_pressure_datum_md: The measure depth datum for
        which the bottomhole pressure is reported.  This will later be
        converted to a TVD for reservoir engineering purpose.
    :ivar bottom_hole_stabilized_pressure: The pressure at the bottom of
        the hole under stabilized conditions (typically at the end of
        the flowing period).
    :ivar bottom_hole_stabilized_temperature: The temperature at the
        bottom of the hole under stabilized conditions (typically at the
        end of the flowing period).
    :ivar casing_head_stabilized_pressure: The pressure at the casing
        head under stabilized conditions (typically at the end of the
        flowing period).
    :ivar casing_head_stabilized_temperature: The temperature at the
        casing head under stabilized conditions (typically at the end of
        the flowing period).
    :ivar tubing_head_stabilized_pressure: The pressure at the tubing
        head under stabilized conditions (typically at the end of the
        flowing period).
    :ivar tubing_head_stabilized_temperature: The temperature at the
        tubing head under stabilized conditions (typically at the end of
        the flowing period).
    :ivar fluid_level: The fluid level achieved in the well. The value
        is given as length units from the well vertical datum.
    :ivar base_usable_water: The lowest usable water depth as measured
        from the surface. See TxRRC H-15.
    """
    choke_orifice_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChokeOrificeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bottom_hole_pressure_datum_md: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BottomHolePressureDatumMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bottom_hole_stabilized_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomHoleStabilizedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bottom_hole_stabilized_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomHoleStabilizedTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    casing_head_stabilized_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "CasingHeadStabilizedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    casing_head_stabilized_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "CasingHeadStabilizedTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tubing_head_stabilized_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "TubingHeadStabilizedPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tubing_head_stabilized_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TubingHeadStabilizedTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_level: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FluidLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    base_usable_water: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BaseUsableWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
