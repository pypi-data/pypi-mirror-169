from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.mass_measure import MassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MassOut:
    """
    The  mass out for this slim tube.

    :ivar mass_effluent_stock_tank_oil: The mass of effluent stock tank
        oil for this slim tube test volume step mass balance.
    :ivar mass_produced_effluent_gas: The mass of produced effluent gas
        for this slim tube test volume step mass balance.
    :ivar mass_residual_oil: The mass of residual oil for this slim tube
        test volume step mass balance.
    :ivar mass_produced_effluent_gas_flow_down: The mass of produced
        effluent gas flow down for this slim tube test volume step mass
        balance.
    :ivar total_mass_out: The total mass out for this slim tube test
        volume step mass balance.
    """
    mass_effluent_stock_tank_oil: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassEffluentStockTankOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_produced_effluent_gas: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassProducedEffluentGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_residual_oil: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassResidualOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_produced_effluent_gas_flow_down: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassProducedEffluentGasFlowDown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_mass_out: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalMassOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
