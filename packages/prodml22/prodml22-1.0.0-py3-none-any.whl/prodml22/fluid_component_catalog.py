from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.formation_water import FormationWater
from prodml22.natural_gas import NaturalGas
from prodml22.plus_fluid_component import PlusFluidComponent
from prodml22.pseudo_fluid_component import PseudoFluidComponent
from prodml22.pure_fluid_component import PureFluidComponent
from prodml22.stock_tank_oil import StockTankOil
from prodml22.sulfur_fluid_component import SulfurFluidComponent

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidComponentCatalog:
    """
    Fluid component catalog.

    :ivar stock_tank_oil: Stock tank oil.
    :ivar natural_gas: Natural gas.
    :ivar formation_water: Formation water.
    :ivar pure_fluid_component: Pure fluid component.
    :ivar pseudo_fluid_component: Pseudo-fluid component.
    :ivar plus_fluid_component: Plus-fluid component.
    :ivar sulfur_fluid_component:
    """
    stock_tank_oil: List[StockTankOil] = field(
        default_factory=list,
        metadata={
            "name": "StockTankOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    natural_gas: List[NaturalGas] = field(
        default_factory=list,
        metadata={
            "name": "NaturalGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    formation_water: List[FormationWater] = field(
        default_factory=list,
        metadata={
            "name": "FormationWater",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pure_fluid_component: List[PureFluidComponent] = field(
        default_factory=list,
        metadata={
            "name": "PureFluidComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pseudo_fluid_component: List[PseudoFluidComponent] = field(
        default_factory=list,
        metadata={
            "name": "PseudoFluidComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    plus_fluid_component: List[PlusFluidComponent] = field(
        default_factory=list,
        metadata={
            "name": "PlusFluidComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sulfur_fluid_component: List[SulfurFluidComponent] = field(
        default_factory=list,
        metadata={
            "name": "SulfurFluidComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
