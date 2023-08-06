from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_dead_model import AbstractCorrelationViscosityDeadModel
from prodml22.apigravity_measure import ApigravityMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeGhettoDead(AbstractCorrelationViscosityDeadModel):
    """
    DeGhetto-Dead.

    :ivar oil_apiat_stock_tank: The oil API at stock tank for the
        viscosity correlation.
    """
    class Meta:
        name = "DeGhetto-Dead"

    oil_apiat_stock_tank: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "OilAPIAtStockTank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
