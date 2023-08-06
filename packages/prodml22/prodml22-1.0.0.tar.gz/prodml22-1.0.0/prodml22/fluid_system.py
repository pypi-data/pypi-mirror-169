from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_temperature_pressure import AbstractTemperaturePressure
from prodml22.data_object_reference import DataObjectReference
from prodml22.formation_water import FormationWater
from prodml22.natural_gas import NaturalGas
from prodml22.phase_present import PhasePresent
from prodml22.reservoir_fluid_kind import ReservoirFluidKind
from prodml22.reservoir_life_cycle_state import ReservoirLifeCycleState
from prodml22.saturation_pressure import SaturationPressure
from prodml22.stock_tank_oil import StockTankOil
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSystem(AbstractObject):
    """Used to designate each distinct subsurface accumulation of economically
    significant fluids.

    This data object primarily serves to identify the source of one or
    more fluid samples and provides a connection to the geologic
    environment that contains it. Characteristics of the fluid system
    include the type of system (e.g., black oil, dry gas, etc.), the
    fluid phases present, and its lifecycle status (e.g., undeveloped,
    producing, etc.).

    :ivar standard_conditions: The standard temperature and pressure
        used for the representation of this fluid system.
    :ivar reservoir_fluid_kind: The kind of reservoir fluid for this
        fluid system. Enum. See reservoir fluid kind.
    :ivar phases_present: The phases present for this fluid system.
        Enum. See phase present.
    :ivar reservoir_life_cycle_state: The reservoir life cycle state for
        this fluid system. Enum. See reservoir life cycle state.
    :ivar rock_fluid_organization_interpretation: Reference to a
        RockFluidOrganizationInterpretation (a RESQML data object).
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        for the fluid system.
    :ivar solution_gor: The solution gas-oil ratio for this fluid
        system.
    :ivar remark: Remarks and comments about this data item.
    :ivar stock_tank_oil: Stock tank oil (STO).
    :ivar formation_water: The water in the formation.
    :ivar natural_gas: Natural gas.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    standard_conditions: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "StandardConditions",
            "type": "Element",
            "required": True,
        }
    )
    reservoir_fluid_kind: Optional[ReservoirFluidKind] = field(
        default=None,
        metadata={
            "name": "ReservoirFluidKind",
            "type": "Element",
            "required": True,
        }
    )
    phases_present: Optional[PhasePresent] = field(
        default=None,
        metadata={
            "name": "PhasesPresent",
            "type": "Element",
        }
    )
    reservoir_life_cycle_state: Optional[ReservoirLifeCycleState] = field(
        default=None,
        metadata={
            "name": "ReservoirLifeCycleState",
            "type": "Element",
        }
    )
    rock_fluid_organization_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RockFluidOrganizationInterpretation",
            "type": "Element",
        }
    )
    saturation_pressure: Optional[SaturationPressure] = field(
        default=None,
        metadata={
            "name": "SaturationPressure",
            "type": "Element",
        }
    )
    solution_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SolutionGOR",
            "type": "Element",
            "required": True,
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
    stock_tank_oil: Optional[StockTankOil] = field(
        default=None,
        metadata={
            "name": "StockTankOil",
            "type": "Element",
        }
    )
    formation_water: Optional[FormationWater] = field(
        default=None,
        metadata={
            "name": "FormationWater",
            "type": "Element",
        }
    )
    natural_gas: Optional[NaturalGas] = field(
        default=None,
        metadata={
            "name": "NaturalGas",
            "type": "Element",
        }
    )
