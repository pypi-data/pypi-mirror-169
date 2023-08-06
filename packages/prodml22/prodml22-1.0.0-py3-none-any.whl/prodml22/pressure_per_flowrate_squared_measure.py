from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.pressure_per_flowrate_squared_uom import PressurePerFlowrateSquaredUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerFlowrateSquaredMeasure:
    """
    PressurePerFlowrateSquared, P/Q^2 is the unit for turbulent flow pressure
    drop in the layer inflow relationship.

    :ivar value:
    :ivar uom: One of uoms from PressurePerFlowrateSquaredUom list
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressurePerFlowrateSquaredUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
