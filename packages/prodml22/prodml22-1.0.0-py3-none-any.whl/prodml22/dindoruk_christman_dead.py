from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_dead_model import AbstractCorrelationViscosityDeadModel
from prodml22.apigravity_measure import ApigravityMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DindorukChristmanDead(AbstractCorrelationViscosityDeadModel):
    """
    DindorukChristman-Dead.

    :ivar oil_gravity_at_stock_tank: The oil gravity at stock tank for
        the viscosity correlation.
    """
    class Meta:
        name = "DindorukChristman-Dead"

    oil_gravity_at_stock_tank: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "OilGravityAtStockTank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
