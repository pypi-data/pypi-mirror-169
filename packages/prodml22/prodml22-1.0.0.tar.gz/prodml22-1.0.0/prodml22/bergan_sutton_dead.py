from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_correlation_viscosity_dead_model import AbstractCorrelationViscosityDeadModel
from prodml22.dynamic_viscosity_measure import DynamicViscosityMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class BerganSuttonDead(AbstractCorrelationViscosityDeadModel):
    """
    BerganSutton-Dead.

    :ivar dead_oil_viscosity_at100_f: The dead oil viscosity at 100 f
        input to the dead oil viscosity model.
    :ivar dead_oil_viscosity_at210_f: The dead oil viscosity at 210 f
        input to the dead oil viscosity model.
    """
    class Meta:
        name = "BerganSutton-Dead"

    dead_oil_viscosity_at100_f: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "DeadOilViscosityAt100F",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    dead_oil_viscosity_at210_f: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "DeadOilViscosityAt210F",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
